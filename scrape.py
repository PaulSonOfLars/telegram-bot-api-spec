import json
import re
import string
import requests
from bs4 import BeautifulSoup
from bs4.element import Tag

TG_CORE_TYPES = ["String", "Boolean", "Integer", "Float"]
ROOT_URL = "https://core.telegram.org"
TO_SCRAPE = {
    "api": ROOT_URL + "/bots/api",
}

METHODS = "methods"
TYPES = "types"

APPROVED_NO_SUBTYPES = {
    "InputFile"
}
APPROVED_MULTI_RETURNS = [
    ['Message', 'Boolean']
]

def retrieve_info(url: str) -> dict:
    r = requests.get(url)
    soup = BeautifulSoup(r.text, features="html5lib")
    dev_rules = soup.find("div", {"id": "dev_page_content"})
    curr_type = ""
    curr_name = ""

    release_tag = dev_rules.find("h4", recursive=False)
    changelog_url = url + release_tag.find("a").get("href")
    version = dev_rules.find("p", recursive=False).get_text()

    items = {
        "version": version,
        "release_date": release_tag.get_text(),
        "changelog": changelog_url,
        METHODS: dict(),
        TYPES: dict(),
    }

    for x in list(dev_rules.children):  
        if x.name == "h3" or x.name == "hr":
            curr_name = ""
            curr_type = ""

        if x.name == "h4":
            anchor = x.find("a")
            name = anchor.get("name")
            if name and "-" in name:
                curr_name = ""
                curr_type = ""
                continue

            curr_name, curr_type = get_type_and_name(x, anchor, items, url)

        if not curr_type or not curr_name:
            continue

        if x.name == "p":
            items[curr_type][curr_name].setdefault("description", []).extend(clean_tg_description(x, url))

        if x.name == "table":
            get_fields(curr_name, curr_type, x, items, url)

        if x.name == "ul":
            get_subtypes(curr_name, curr_type, x, items, url)

        if curr_type == METHODS and items[curr_type][curr_name].get("description"):
            get_method_return_type(curr_name, curr_type, items[curr_type][curr_name].get("description"), items)

    return items

def get_subtypes(curr_name: str, curr_type: str, x: Tag, items: dict, url: str):
    if curr_name == "InputFile":
        return

    list_contents = []
    for li in x.find_all("li"):
        list_contents.extend(clean_tg_description(li, url))

    if curr_type == TYPES:
        items[curr_type][curr_name]["subtypes"] = list_contents

    items[curr_type][curr_name]["description"] += [f"- {s}" for s in list_contents]

def get_fields(curr_name: str, curr_type: str, x: Tag, items: dict, url: str):
    body = x.find("tbody")
    fields = []
    for tr in body.find_all("tr"):
        children = list(tr.find_all("td"))
        if curr_type == TYPES and len(children) == 3:
            desc = clean_tg_field_description(children[2], url)
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
                    "description": clean_tg_field_description(children[3], url)
                }
            )

    items[curr_type][curr_name]["fields"] = fields

def get_method_return_type(curr_name: str, curr_type: str, description_items: list[str], items: dict):
    description = "\n".join(description_items)
    ret_search = re.search("(?:on success,)([^.]*)", description, re.IGNORECASE)
    ret_search2 = re.search("(?:returns)([^.]*)(?:on success)?", description, re.IGNORECASE)
    ret_search3 = re.search("([^.]*)(?:is returned)", description, re.IGNORECASE)
    if ret_search:
        extract_return_type(curr_type, curr_name, ret_search.group(1).strip(), items)
    elif ret_search2:
        extract_return_type(curr_type, curr_name, ret_search2.group(1).strip(), items)
    elif ret_search3:
        extract_return_type(curr_type, curr_name, ret_search3.group(1).strip(), items)

def get_type_and_name(t: Tag, anchor: Tag, items: dict, url: str):
    if t.text[0].isupper():
        curr_type = TYPES
    else:
        curr_type = METHODS
    curr_name = t.get_text()
    items[curr_type][curr_name] = {"name": curr_name}

    href = anchor.get("href")
    if href:
        items[curr_type][curr_name]["href"] = url + href

    return curr_name, curr_type

def extract_return_type(curr_type: str, curr_name: str, ret_str: str, items: dict):
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

def clean_tg_field_description(t: Tag, url: str) -> str:
    return " ".join(clean_tg_description(t, url))

def clean_tg_description(t: Tag, url: str) -> list[str]:
    for i in t.find_all("img"):
        i.replace_with(i.get("alt"))

    for br in t.find_all("br"):
        br.replace_with("\n")

    for a in t.find_all("a"):
        anchor_text = a.get_text()
        if "»" not in anchor_text:
            continue

        link = a.get("href")
        if link.startswith("#"):
            link = url + link
        elif link.startswith("/"):
            link = ROOT_URL + link

        anchor_text = anchor_text.replace(" »", ": " + link)
        a.replace_with(anchor_text)

    text = t.get_text()
    text = re.sub(r"(\s){2,}", r"\1", text)
    text = text.replace('”', '"').replace('“', '"')
    text = text.replace("…", "...")
    text = text.replace(u"\u2013", "-")
    text = text.replace(u"\u2014", "-")
    text = text.replace(u"\u2019", "'")

    return [t.strip() for t in text.split("\n") if t.strip()]

def clean_tg_type(t: str) -> list[str]:
    pref = ""
    if t.startswith("Array of "):
        pref = "Array of "
        t = t[len("Array of "):]

    fixed_ors = [x.strip() for x in t.split(" or ")]
    fixed_ands = [x.strip() for fo in fixed_ors for x in fo.split(" and ")]
    fixed_commas = [x.strip() for fa in fixed_ands for x in fa.split(", ")]
    return [pref + get_proper_type(x) for x in fixed_commas]

def get_proper_type(t: str) -> str:
    if t == "Messages":
        return "Message"
    elif t == "Float number":
        return "Float"
    elif t == "Int":
        return "Integer"
    elif t == "True" or t == "Bool":
        return "Boolean"
    return t


def write_to_markdown(items: dict, filename: str):
    with open(filename, "w") as f:
        # Header Section
        f.write(f"# 📖 Telegram Bot API Documentation\n")
        f.write(f"**Version**: `{items['version']}`\n")
        f.write(f"**Release Date**: `{items['release_date']}`\n")
        f.write(f"[🔗 Changelog]({items['changelog']})\n")
        f.write(f"\n---\n")  # Line separator

        # Preface for Methods and Types
        f.write("## ✨ Introduction\n")
        f.write("This document contains the detailed specifications of the Telegram Bot API, including methods and types.\n")
        f.write("You can quickly navigate to the specific methods or types by clicking on the links below:\n")

        # Method Links
        f.write("### 🚀 Methods\n")
        for method in items[METHODS]:
            method_id = method.lower().replace(" ", "-")
            f.write(f"- [{method}](#{method_id})\n")

        # Type Links
        f.write("### 🛠️ Types\n")
        for t_type in items[TYPES]:
            type_id = t_type.lower().replace(" ", "-")
            f.write(f"- [{t_type}](#{type_id})\n")

        f.write("\n---\n")  # Line separator

        # Methods Section
        f.write("## 🚀 Methods\n")
        for method, details in items[METHODS].items():
            method_id = method.lower().replace(" ", "-")  # Generate a unique ID for the method
            f.write(f"### ⚙️ {method} <a id='{method_id}'></a>\n")  # Add a unique ID
            f.write(f"- **URL**: [{details['href']}]({details['href']})\n")
            f.write("- **Description**:\n")
            for desc in details.get("description", []):
                f.write(f"  - {desc}\n")
            if details.get("fields"):
                f.write("- **Fields**:\n")
                for field in details["fields"]:
                    f.write(f"  - **{field['name']}**: {', '.join(field['types'])} (Required: {field['required']})\n")
                    f.write(f"    - {field['description']}\n")
            if details.get("returns"):
                f.write(f"- **Returns**: {', '.join(details['returns'])}\n")
            f.write(f"\n---\n\n")

        # Types Section
        f.write("## 🛠️ Types\n")
        for t_type, details in items[TYPES].items():
            type_id = t_type.lower().replace(" ", "-")  # Generate a unique ID for the type
            f.write(f"### 📦 {t_type} <a id='{type_id}'></a>\n")  # Add a unique ID
            f.write(f"- **URL**: [{details['href']}]({details['href']})\n")
            f.write("- **Description**:\n")
            for desc in details.get("description", []):
                f.write(f"  - {desc}\n")
            if details.get("fields"):
                f.write("- **Fields**:\n")
                for field in details["fields"]:
                    f.write(f"  - **{field['name']}**: {', '.join(field['types'])} (Required: {field['required']})\n")
                    f.write(f"    - {field['description']}\n")
            if details.get("subtypes"):
                f.write("- **Subtypes**:\n")
                for subtype in details["subtypes"]:
                    f.write(f"  - {subtype}\n")

            f.write(f"\n---\n\n")

        # Final separator
        f.write("\n---\n")
        f.write("📝 *Documentation auto-generated by Telegram Bot API Scraper*\n")




def main():
    items = retrieve_info(TO_SCRAPE["api"])
    write_to_markdown(items, "api_docs.md")

if __name__ == "__main__":
    main()
