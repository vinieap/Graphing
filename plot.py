from Point import Point
import matplotlib.pyplot as plt
from random import randint

NUM_POINTS = 1_000_000

LOWER_X = -1_000_000_000
UPPER_X = 1_000_000_000
LOWER_Y = -1_000_000_000
UPPER_Y = 1_000_000_000

points = [Point(randint(LOWER_X, UPPER_X), randint(LOWER_Y, UPPER_Y)) for _ in range(NUM_POINTS)]

plt.scatter(*zip(*points), s=1)

plt.show()