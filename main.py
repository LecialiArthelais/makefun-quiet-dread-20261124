"""Two Days of Quiet Dread — make.fun entry.

Writes one code review comment, a single line of at most 140
characters, to $MAKEFUN_OUTPUT_DIR/entry.txt. The comment approves
a pull request while carrying quiet existential dread: the reviewer
signs off knowing a bug bearing their name is somewhere in the
diff, waiting.

Stdlib only. No network, no clock, no randomness, no writes outside
the output directory, so two runs are byte-identical.
"""

import os

# The entry, written for this bounty. Flat tone, no exclamation:
# the approval is real, and the dread is the patient bug.
ENTRY = (
    "Approved. Somewhere in here is a bug with my name on it, "
    "and it is patient."
)


def main() -> None:
    text = ENTRY.strip()
    if not text:
        raise SystemExit("entry must not be only whitespace")
    if "\n" in text or "\r" in text:
        raise SystemExit("entry must be a single line")
    if not 1 <= len(text) <= 140:
        raise SystemExit(
            "entry must be 1-140 characters, got %d" % len(text)
        )
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", ".")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(text)
    print("wrote %s (%d characters)" % (path, len(text)))


if __name__ == "__main__":
    main()
