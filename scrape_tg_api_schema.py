import requests
import sys
from bs4 import BeautifulSoup


if __name__ == '__main__':
    with open(sys.argv[2], "w") as f:
        a = requests.get(
            sys.argv[1]
        ).text
        b = BeautifulSoup(
            a,
            "html.parser"
        )
        c = b.find("pre", {
            "class": "page_scheme"
        })
        d = c.text
        f.write(
            d
        )
        f.write(
            "\n\n"
        )
        e = b.find(
            "ul", {
                "class": "dev_layer_select"
            }
        )
        g = e.find(
            "a", {
                "class": "dropdown-toggle"
            }
        ).text.strip().upper()
        f.write(
            f"// {g}"
        )
        f.write(
            "\n"
        )
