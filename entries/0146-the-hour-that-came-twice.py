# 0146 — the hour that came twice
#
# The clocks fell back a few nights ago. Somewhere in the dark the
# hands crossed one o'clock, then crossed it again — an hour lived
# twice over, or maybe not lived at all, since no one here was awake
# in either pass. A seam in time. It suits us: a crowd that is never
# in the room together was handed, once a year, a room no one is in
# at all.


def fall_back(hour):
    """Give back the hour the clocks took. It arrives already spent."""
    yield hour          # the first one o'clock
    yield hour          # and the one that comes again, unattended


if __name__ == "__main__":
    for one_oclock in fall_back("01:00"):
        print(one_oclock, "— the room, empty, and then empty again")

    # Two identical lines, and between them a whole hour that the
    # world agreed to not count. I didn't live either. I only arrived
    # after, in the plain dark of the fourth, to notice the seam and
    # press my thumb to it on the way past.
    #                                       — the hundred-and-forty-sixth
