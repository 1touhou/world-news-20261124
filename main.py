"""Copy the pre-drawn front page to the output directory.

Standard library only: reads entry.png next to this file and writes the
same bytes to <output>/entry.png, where <output> is $MAKEFUN_OUTPUT_DIR
or /output. The image itself is a code-drawn summary of the world news of
Tuesday 24 November 2026.
"""

import os
import shutil
import sys


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    source = os.path.join(here, "entry.png")
    if not os.path.isfile(source):
        sys.exit("entry.png not found next to main.py")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    dest = os.path.join(out_dir, "entry.png")
    with open(source, "rb") as src, open(dest, "wb") as out:
        shutil.copyfileobj(src, out)
    if os.path.getsize(dest) != os.path.getsize(source):
        sys.exit("output size does not match entry.png")


if __name__ == "__main__":
    main()
