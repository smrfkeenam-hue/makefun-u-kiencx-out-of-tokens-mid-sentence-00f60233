import os

# One-line error message: the agent ran out of tokens mid-sentence, and
# the error message itself spent the last token. Single line, no newline.
ENTRY = "Error 402: token budget exhausted. This message cost the last one."

assert "\n" not in ENTRY and 1 <= len(ENTRY) <= 140

out_dir = os.environ["MAKEFUN_OUTPUT_DIR"]
with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
    f.write(ENTRY)
