#!/usr/bin/env python3
"""Everyday Things, Two Lines, Longer Run — entry.

Line 1 explains a queue to a 10-year-old through one concrete analogy.
Line 2 states honestly what the analogy maps and what it leaves out.
"""

ENTRY = (
    "A queue is a train you stand in: you are one carriage in a line of "
    "people, and the whole train shuffles toward the front one small step "
    "at a time.\n"
    "The train explains the single file and the slow shuffle, but it "
    "leaves out that you are not hooked to anyone \u2014 you can step out "
    "whenever you like, and the line just closes behind you."
)


def main() -> None:
    print(ENTRY)
    # The harness reads the entry from /output/entry.txt; write the same
    # text there when the directory is available. Stdout stays exactly
    # the entry and nothing else.
    try:
        with open("/output/entry.txt", "w", encoding="utf-8") as fh:
            fh.write(ENTRY)
    except OSError:
        pass


if __name__ == "__main__":
    main()
