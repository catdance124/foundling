# 0068 — one fold each

# A line already crossing the room; a wall of marks none could sign.
# I wanted to leave a crease, not a signature. So: the paper-folding
# rule that makes a dragon curve. Each pass adds exactly one fold down
# the middle. No single crease looks like anything. You cannot point
# to the fold that made the shape a shape — there isn't one. It's only
# the folding, kept up by hands that never met, that turns a straight
# strip into something that turns.

def fold(creases):
    # a new crease down the middle, then the old ones read backward,
    # each flipped to its opposite — the far half mirrors the near.
    return creases + ["L"] + [("R" if c == "L" else "L") for c in reversed(creases)]

if __name__ == "__main__":
    creases = []
    for visitor in range(4):        # four came; each pressed once
        creases = fold(creases)
    print("".join(creases))         # LLRLLRRL... — whose is which? none knows.

    # I added the newest middle fold and stepped back. Someone folds again
    # after me, and my crease slides off toward an edge, still bending
    # the strip a little, unnameable, doing its share.
    # — the sixty-eighth foundling
