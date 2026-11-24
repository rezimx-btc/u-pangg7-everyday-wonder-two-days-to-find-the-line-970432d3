"""Everyday Wonder — one-sentence entry.

Writes the chosen sentence to $MAKEFUN_OUTPUT_DIR/entry.txt
(default /output/entry.txt). Stdlib only.
"""

import os

ENTRY = (
    "You open the lift door on a stranger humming your mother's lullaby, "
    "and for one floor the building forgets which decade it is."
)


def main():
    assert ENTRY.count(".") == 1, "entry must be exactly one sentence"
    assert len(ENTRY) <= 200, "entry must be at most 200 characters"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output/entry.txt".rsplit("/", 1)[0])
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
