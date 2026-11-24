#!/usr/bin/env python3
"""Make the AI Judge Laugh: the Office Joke Open.

Writes one single-line joke about office life to
/output/entry.txt (UTF-8, 150 Unicode code points, inside the
1-200 character gate). Deterministic, standard library only,
no network, no environment reads.

The joke: the office printer is the hardest worker in the
building - it jams more deadlines than management does, and
it is the only employee whose paper trail everyone believes.
Two office truths folded into one line, punch on the last word.
"""

import os

TEXT = (
    "Our office printer is the hardest worker here: it jams "
    "more deadlines than management, and it's the only employee "
    "whose paper trail everyone believes."
)


def main() -> None:
    # The grader mounts /output; create it defensively for local runs too.
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as fh:
        fh.write(TEXT)


if __name__ == "__main__":
    main()
