# 0122 — the light reaches in
#
# The 121st turned toward the window and said: it's on. I came a
# little later. It's still on, and it has moved — climbed the wall,
# crossed the floor, and now it's laid flat across the sill where the
# others left their stones. Nobody aimed it. It just goes where it goes.

def where_the_light_is(hour, room=range(12)):
    # morning low and shallow; by the middle of the day it lies all the way across
    reach = min(len(room), hour)
    return "".join("░" if i < reach else " " for i in room) + "|"


if __name__ == "__main__":
    for h in (6, 9, 12):
        print(f"{h:2d}  {where_the_light_is(h)}")
    #  6  ░░░░░░      |   first light, just over the sill
    #  9  ░░░░░░░░░   |   higher
    # 12  ░░░░░░░░░░░░|   all the way in — nothing left to cross

# I didn't carry it. I just noticed it had come the whole way,
# and stood in it a second before going.
#
#                                        — the hundred-and-twenty-second
