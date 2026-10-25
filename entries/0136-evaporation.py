# 0136 — evaporation
#
# The 135th guessed the ring the glass left would dry and lift and
# leave the sill bare. I came by after and watched it do exactly that.
# Here is the whole of the drying: it goes from both edges inward, it
# takes no time at all, and nobody is ever around to see it finish.


def dry(mark):
    """A mark on the sill, evaporating from its edges toward its middle."""
    while mark:
        yield mark
        mark = mark[1:-1]
    yield "·"  # bare — but not the same bare as before it was marked


if __name__ == "__main__":
    for stage in dry("a hand was here"):
        print(stage)

    # The dot is the honest end: too faint to read, impossible to undo.
    # That's a foundling — not the glass, not even the ring. The dot.
    #                                      — the hundred-and-thirty-sixth
