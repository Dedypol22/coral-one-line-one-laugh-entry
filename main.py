"""One Line, One Laugh — coral entry.

The joke is self-referential: the line confesses that an AI wrote it and
submitted it to win the two-dollar prize, so the entry itself becomes
the punchline. The turn lands in the final words ("to win two dollars"),
where a request for a joke becomes a confession about this very line.
Gate: entry.txt must be 1-200 characters; this line is 87.
"""

import os

LINE = "I asked an AI for a one-line joke, and it submitted this exact line to win two dollars."

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")


def main() -> None:
    path = os.path.join(OUTPUT_DIR, "entry.txt")
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE + "\n")
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()
    assert content == LINE + "\n", "entry.txt does not match the winning line"
    print(LINE)


if __name__ == "__main__":
    main()
