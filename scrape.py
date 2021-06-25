import json
import re
import string
from typing import List, Dict

import requests
from bs4 import BeautifulSoup

TG_CORE_TYPES = ["String", "Boolean", "Integer", "Float"]
API_URL = "https://core.telegram.org/bots/api"

METHODS = "methods"
TYPES = "types"


def retrieve_api_info() -> Dict:
    r = requests.get(API_URL)
    soup = BeautifulSoup(r.text, features="html.parser")
    dev_rules = soup.find("div", {"id": "dev_page_content"})
    curr_type = ""
    curr_name = ""
    curr_desc = []

    items = {
        METHODS: dict(),
        TYPES: dict(),
    }

    for x in list(dev_rules.children):
        if x.name == "h3":
            # New category; clear name and type.
            curr_name = ""
            curr_type = ""
            curr_desc = []

        if x.name == "h4":
            anchor = x.find("a")
            name = anchor.get("name")
            if name and "-" in name:
                curr_name = ""
                curr_type = ""
                curr_desc = []
                continue

            curr_name, curr_type = get_type_and_name(x, anchor, items)
            curr_desc = []

        if not curr_type or not curr_name:
            continue

        if x.name == "p":
            description = x.get_text().strip()
            # we only need returns for methods.
            # We only check this when curr_desc is empty, since the first paragraph contains the description.
            if curr_type == METHODS and not curr_desc:
                get_method_return_type(curr_name, curr_type, description, items)

            curr_desc.append(description)
            items[curr_type][curr_name]["description"] = curr_desc

        if x.name == "table":
            get_fields(curr_name, curr_type, x, items)

        if x.name == "ul":
            get_subtypes(curr_name, curr_type, x, items)

    return items


def get_subtypes(curr_name: str, curr_type: str, x, items: dict):
    if curr_name == "InputFile":  # Has no interesting subtypes
        return

    subtypes = []
    for li in x.find_all("li"):
        subtype_name = li.get_text()
        subtypes.append(subtype_name)

    items[curr_type][curr_name]["subtypes"] = subtypes


# Get fields/parameters of type/method
def get_fields(curr_name: str, curr_type: str, x, items: dict):
    body = x.find("tbody")
    fields = []
    for tr in body.find_all("tr"):
        children = list(tr.find_all("td"))
        if curr_type == TYPES and len(children) == 3:
            desc = clean_tg_description(children[2].get_text())
            fields.append(
                {
                    "name": children[0].get_text(),
                    "types": clean_tg_type(children[1].get_text()),
                    "required": not desc.startswith("Optional. "),
                    "description": desc,
                }
            )

        elif curr_type == METHODS and len(children) == 4:
            fields.append(
                {
                    "name": children[0].get_text(),
                    "types": clean_tg_type(children[1].get_text()),
                    "required": children[2].get_text() == "Yes",
                    "description": clean_tg_description(children[3].get_text()),
                }
            )

        else:
            print("An unexpected state has occurred!")
            print("Type:", curr_type)
            print("Name:", curr_name)
            print("Number of children:", len(children))
            print(children)
            exit(1)

    items[curr_type][curr_name]["fields"] = fields


def get_method_return_type(curr_name, curr_type, description, items):
    ret_search = re.search("(?:on success,|returns)([^.]*)(?:on success)?", description, re.IGNORECASE)
    ret_search2 = re.search("([^.]*)(?:is returned)", description, re.IGNORECASE)
    if ret_search:
        extract_return_type(curr_type, curr_name, ret_search.group(1).strip(), items)
    elif ret_search2:
        extract_return_type(curr_type, curr_name, ret_search2.group(1).strip(), items)
    else:
        print("Failed to get return type for", curr_name)


def get_type_and_name(x, anchor, items):
    if x.text[0].isupper():
        curr_type = TYPES
    else:
        curr_type = METHODS
    curr_name = x.get_text()
    items[curr_type][curr_name] = {"name": curr_name}

    href = anchor.get("href")
    if href:
        items[curr_type][curr_name]["href"] = API_URL + href

    return curr_name, curr_type


def extract_return_type(curr_type: str, curr_name: str, ret_str: str, items: Dict):
    array_match = re.search(r"(?:array of )+(\w*)", ret_str, re.IGNORECASE)
    if array_match:
        ret = clean_tg_type(array_match.group(1))
        rets = [f"Array of {r}" for r in ret]
        items[curr_type][curr_name]["returns"] = rets
    else:
        words = ret_str.split()
        rets = [
            r for ret in words
            for r in clean_tg_type(ret.translate(str.maketrans("", "", string.punctuation)))
            if ret[0].isupper()
        ]
        items[curr_type][curr_name]["returns"] = rets


def clean_tg_description(t: str) -> str:
    return t.replace('”', '"').replace('“', '"')


def get_proper_type(t: str) -> str:
    if t == "Messages":  # Avoids https://core.telegram.org/bots/api#sendmediagroup
        return "Message"

    elif t == "Float number":
        return "Float"

    elif t == "Int":
        return "Integer"

    elif t == "True" or t == "Bool":
        return "Boolean"

    return t


def clean_tg_type(t: str) -> List[str]:
    pref = ""
    if t.startswith("Array of "):
        pref = "Array of "
        t = t[len("Array of "):]

    fixed_ors = [x.strip() for x in t.split(" or ")]  # Fix situations like "A or B"
    fixed_ands = [x.strip() for fo in fixed_ors for x in fo.split(" and ")]  # Fix situations like "A and B"
    fixed_commas = [x.strip() for fa in fixed_ands for x in fa.split(", ")]  # Fix situations like "A, B"
    return [pref + get_proper_type(x) for x in fixed_commas]


def verify_type_parameters(items: Dict):
    for t, values in items[TYPES].items():
        # check all values have a URL
        if not values.get("href"):
            print(f"{t} has no link!")
            continue

        fields = values.get("fields", [])
        if len(fields) == 0:
            subtypes = values.get("subtypes", [])
            if not subtypes:
                print("TYPE", t, "HAS NO FIELDS OR SUBTYPES")
                continue

            for st in subtypes:
                if st in items[TYPES]:
                    if "subtype_of" in items[TYPES][st]:
                        items[TYPES][st]["subtype_of"].append(t)
                    else:
                        items[TYPES][st]["subtype_of"] = [t]
                else:
                    print("TYPE", t, "USES INVALID SUBTYPE", st)

        # check all parameter types are valid
        for param in fields:
            types = param.get("types")
            for t in types:
                while t.startswith("Array of "):
                    t = t[len("Array of "):]

            if t not in items[TYPES] and t not in TG_CORE_TYPES:
                print("UNKNOWN FIELD TYPE", t)


def verify_method_parameters(items: Dict):
    # Type check all methods
    for method, values in items[METHODS].items():
        # check all values have a URL
        if not values.get("href"):
            print(f"{method} has no link!")
            continue

        # check all methods have a return
        if not values.get("returns"):
            print(f"{method} has no return types!")
            continue

        if len(values.get("returns")) > 1:
            print(f"{method} has multiple return types: {values.get('returns')}")

        # check all parameter types are valid
        for param in values.get("fields", []):
            types = param.get("types")
            for t in types:
                while t.startswith("Array of "):
                    t = t[len("Array of "):]

                if t not in items[TYPES] and t not in TG_CORE_TYPES:
                    print("UNKNOWN PARAM TYPE", t)

        # check all return types are valid
        for ret in values.get("returns", []):
            while ret.startswith("Array of "):
                ret = ret[len("Array of "):]

            if ret not in items[TYPES] and ret not in TG_CORE_TYPES:
                print("UNKNOWN RETURN TYPE", ret)


if __name__ == '__main__':
    ITEMS = retrieve_api_info()
    verify_type_parameters(ITEMS)
    verify_method_parameters(ITEMS)

    with open("api.json", "w") as f:
        json.dump(ITEMS, f, indent=2)
