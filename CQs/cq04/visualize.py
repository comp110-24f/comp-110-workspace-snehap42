"""CQ04 Visualize"""

__author__ = "730740674"

from CQs.cq04.concatenation import concat  # imports function from concatenation module
from CQs.cq04.coordinates import get_coords  # imports function from coordinates module

x = "123"
y = "abc"

print(concat(x, y))
print(get_coords(x, y))
