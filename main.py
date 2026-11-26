#!/usr/bin/env python3
"""The Worst Pizza Topping — make.fun bounty u-motasimfuad-the-worst-pizza-topping-062c6893.

Writes one funny line pitching a terrible pizza topping to /output/entry.txt.
The line must be 1-200 characters, a single line, naming a pizza and a topping
and landing a real joke with a surprising turn (per the judge brief: terrible
topping first, funny second, vivid and specific, sounds like a sales pitch).

The topping: wet cement. Terrible because it literally sets into a patio —
a concrete image with a concrete twist, sold like a limited-time offer.
"""

import os

LINE = "Try our new pizza topped with wet cement \u2014 it sets in 20 minutes, so eat fast or dinner becomes a patio."


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
