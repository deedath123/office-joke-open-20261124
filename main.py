"""Office joke entry for make.fun — Make the AI Judge Laugh: the Office Joke Open.

Verified entry line (137 chars):
"HR told me to stop writing 'per my last email'. I replied with a 214-word
explanation of why I can't stop. It began: 'Per my last email.'"

Writes the line verbatim to entry.txt inside MAKEFUN_OUTPUT_DIR
(fallback /output).
"""

import os
import sys

ENTRY = (
    "HR told me to stop writing 'per my last email'. "
    "I replied with a 214-word explanation of why I can't stop. "
    "It began: 'Per my last email.'"
)


def main():
    assert 1 <= len(ENTRY) <= 200, "entry must be 1-200 chars"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(f"Wrote {len(ENTRY)} chars to {path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
