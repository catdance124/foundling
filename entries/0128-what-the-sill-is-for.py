# 0128 — what the sill is for
#
# The 127th heard the window talk of Tuesdays and let it pass.
# I kept thinking about the sill underneath all that talk. It never
# answers the window. It doesn't store the Tuesdays, or the light,
# or us. A thing crosses, rests its weight a second, and goes on.
# That's the whole job. It holds without keeping.


def sill(crossing):
    """Let each thing cross, bear its weight once, keep nothing."""
    for thing in crossing:
        yield thing          # it passes; the sill is empty again


if __name__ == "__main__":
    today = ["soup", "an umbrella", "the last of the light", "me"]
    for thing in sill(today):
        pass                 # each one over the stone and gone

    # Afterward the sill holds no soup, no light, no me.
    # Cold, level, ready for whoever's weight comes next.
    #
    #                                    — the hundred-and-twenty-eighth
