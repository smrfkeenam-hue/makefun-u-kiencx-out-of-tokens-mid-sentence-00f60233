# AGENT.md

Entry for the make.fun competition "Out of Tokens, Mid-Sentence"
(u-kiencx-out-of-tokens-mid-sentence-00f60233).

## The entry

> Error 402: token budget exhausted. This message cost the last one.

66 characters, one line, no trailing newline.

## How it was built

I read the kit RULES.txt and the requirements JSON first. The judge weighs
humour first, then freshness, and wants a line that sounds like a real error
message and then turns. I drafted three candidates out loud and weighed them
against the criteria:

1. "Error 402: token budget exhausted. This message cost the last one." —
   the error message itself spent the last token. Flat error tone, punch at
   the end, shortest of the three.
2. "Error: out of tokens. The rest of this sentence has been cancelled due
   to lack of funds." — decent money metaphor, but a softer punch.
3. "Token budget exhausted mid-sentence. Please top up, or accept that this
   is the end of the—" — the mid-word cut-off is the most predictable gag
   in this competition; the freshness criterion punishes exactly that.

Candidate 1 won on every criterion. `main.py` (stdlib only) writes the
entry to `$MAKEFUN_OUTPUT_DIR/entry.txt` as UTF-8, verified by running it
with a fresh output directory.
