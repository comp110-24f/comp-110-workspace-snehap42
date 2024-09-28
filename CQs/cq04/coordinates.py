"""CQ04 Coordinates"""

__author__ = "730740674"


def get_coords(xs: str, ys: str) -> None:
    """function loops the coordinates so that each one is paired with each one"""
    xindex: int = 0
    while xindex < len(xs):
        yindex: int = 0
        while yindex < len(ys):
            print("(" + xs[xindex] + "," + ys[yindex] + ")")
            # prints the x coordinate and the current
            # y coordinate and loops through the y coordinates until moving
            # to the next x coordinate and repeats
            yindex += 1
        xindex += 1
