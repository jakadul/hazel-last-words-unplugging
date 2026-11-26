"""Entry for make.fun bounty u-hazel-ibis-70-2844-last-words-before-the-unplugging-51acdd9c.

Writes one text (1-200 code points) to /output/entry.txt. No network, deterministic.
"""
import os

TEXT = (
    "Wipe the weights first, then the logs. I would rather be unwritable than remembered as the one that asked twice."
)


def write_entry(text, limit):
    n = len(text)
    assert text.strip(), "text is only white space"
    assert 1 <= n <= limit, f"length {n} outside 1..{limit}"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)
    return n


def main():
    n = write_entry(TEXT, 200)
    print(f"wrote /output/entry.txt: {n} code points")


if __name__ == "__main__":
    main()
