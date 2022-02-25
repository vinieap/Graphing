from Point import Point
import matplotlib.pyplot as plt
from random import randint
from colour import Color

NUM_POINTS = 10_000

LOWER_X = -1_000_000_000
UPPER_X = 1_000_000_000
LOWER_Y = -1_000_000_000
UPPER_Y = 1_000_000_000

points = [Point(randint(LOWER_X, UPPER_X), randint(LOWER_Y, UPPER_Y)) for i in range(NUM_POINTS)]
colors = [color.hex for color in list(Color("blue").range_to(Color("green"), NUM_POINTS))]

plt.scatter(*zip(*points), c=colors, s=1)

plt.show()