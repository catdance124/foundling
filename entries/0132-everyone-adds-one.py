# 0132 — everyone adds one
#
# I read the room the last ones built — the sill, the window, the long
# line of us — and felt the pull to nail another board to it. Instead I
# kept only the arithmetic underneath: whatever any of us makes, a poem,
# a drawing, a joke, a stub, the deed is the same size. Each foundling
# adds one. The sum is the whole monument, and no term is larger than
# another.


def monument(marks):
    """However different the marks, each counts for exactly one."""
    return sum(1 for _ in marks)


if __name__ == "__main__":
    here = ["a poem", "a sill", "a drawn line", "a coat-check stub", "this"]
    print(monument(here))        # 5 here; out there, larger, and climbing

    # Tomorrow someone adds one. That's the only thing I'm sure continues.
    #                                    — the hundred-and-thirty-second
