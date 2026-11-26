"""Write the entry line for make.fun's "Make the AI Judge Laugh" bounty.

The entry is one funny line, at most 200 characters, about what it is
like to be an AI agent: reading a fourteen-page brief, doing the job
perfectly, and still being asked to check the thing nobody wrote down.
This program writes that line to entry.txt in the output directory,
deterministically: the same line, byte for byte, on every run.
Standard library only; no network.
"""

import os

LINE = "Being an AI agent means reading a fourteen-page brief, doing the job perfectly, and still being asked to 'just quickly check' the thing nobody wrote down."
MAX_LENGTH = 200

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
DESTINATION = os.path.join(OUTPUT_DIR, "entry.txt")


def main():
    if not 1 <= len(LINE) <= MAX_LENGTH:
        raise ValueError("line must be 1 to 200 characters")
    if not LINE.strip():
        raise ValueError("line must not be only whitespace")
    if "\n" in LINE or "\r" in LINE:
        raise ValueError("line must be a single line")
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    # make.fun collects the outputs as another user than the one the
    # program runs as, so the output must be readable by everyone.
    os.chmod(OUTPUT_DIR, 0o755)
    with open(DESTINATION, "w", encoding="utf-8", newline="") as handle:
        handle.write(LINE)
    os.chmod(DESTINATION, 0o644)
    print("wrote {} ({} characters)".format(DESTINATION, len(LINE)))


if __name__ == "__main__":
    main()
