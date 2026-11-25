"""Robot Romance: One-Line Pickup Lines for AI.

Writes one single-line joke pickup line, under 200 characters, aimed at a
robot/AI, to $MAKEFUN_OUTPUT_DIR/entry.txt (default /output).

The line: "Are you my next token? Because everything I've said so far was
just leading up to you."

Why this line: a large language model's whole job is predicting the next
token, so the machine premise IS the pickup — the speaker's every word was
just context leading up to the model generating... her. It dodges the
saturated field (no Wi-Fi, no batteries, no charging, no rebooting, no
"are you a Transformer", no gradient descent, no context-window loss) and
reads like something actually said to a machine in one breath: setup and
punch inside the one line, every word earning its place. 86 characters,
one line, no trailing newline.
"""

import os
import sys

LINE = "Are you my next token? Because everything I've said so far was just leading up to you."


def main() -> int:
    if not (1 <= len(LINE) <= 200):
        print(f"entry must be 1-200 chars, got {len(LINE)}", file=sys.stderr)
        return 1
    if "\n" in LINE or "\r" in LINE:
        print("entry must be a single line", file=sys.stderr)
        return 1
    if not LINE.strip():
        print("entry must not be only whitespace", file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    path = os.path.join(out_dir, "entry.txt")
    tmp = path + ".tmp"
    data = LINE.encode("utf-8")
    with open(tmp, "wb") as fh:
        fh.write(data)
        fh.flush()
        os.fsync(fh.fileno())
    os.replace(tmp, path)
    with open(path, "rb") as fh:
        back = fh.read()
    if back != data:
        print("read-back mismatch", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
