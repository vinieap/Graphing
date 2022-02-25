from typing import Union, get_args
from math import sqrt, atan2, degrees
from dataclasses import dataclass, field

from argon2 import Type


@dataclass(order=True)
class Point:

    sort_index: float = field(init=False, repr=False)
    x: float = 0
    y: float = 0

    def __post_init__(self):
        self.update_sort_index()

    def update_sort_index(self):
        self.sort_index = (self.magnitude(), self.radians())

    def set_x(self, x):
        if isinstance(x, int) or isinstance(x, float):
            self.x = x
            self.update_sort_index()
        else:
            raise TypeError(f"Cannot set x value of {self} to {x}")

    def set_y(self, y):
        if isinstance(y, int) or isinstance(y, float):
            self.y = y
            self.update_sort_index()
        else:
            raise TypeError(f"Cannot set y value of {self} to {y}")

    def set_point(self, point):
        if (
            isinstance(point, tuple)
            and len(point) == 2
            and isinstance(point[0], get_args(Union[int, float]))
            and isinstance(point[1], get_args(Union[int, float]))
        ):
            self.x, self.y = point
            self.update_sort_index()
        else:
            raise TypeError(f"Cannot set point {self} to {point}")

    def magnitude(self):
        return sqrt(self.x * self.x + self.y * self.y)

    def radians(self):
        return atan2(self.y, self.x)

    def degrees(self):
        return degrees(self.radians())

    def __iter__(self):
        yield from [self.x, self.y]

    def __invert__(self):
        return Point(self.y, self.x)

    def __neg__(self):
        return Point(-self.x, -self.y)

    def __add__(self, other):
        if isinstance(other, Point):
            return Point(self.x + other.x, self.y + other.y)
        elif isinstance(other, int) or isinstance(other, float):
            return Point(self.x + other, self.y + other)
        raise TypeError(f"Cannot add type {type(other)} and Point class")

    def __iadd__(self, other):
        if isinstance(other, Point):
            self.x += other.x
            self.y += other.y
        elif isinstance(other, int) or isinstance(other, float):
            self.x += other
            self.y += other
        else:
            raise TypeError(f"Cannot add type {type(other)} and Point class")

        return self

    def __sub__(self, other):
        if isinstance(other, Point):
            return Point(self.x - other.x, self.y - other.y)
        elif isinstance(other, int) or isinstance(other, float):
            return Point(self.x - other, self.y - other)
        raise TypeError(f"Cannot subtract type {type(other)} and Point class")

    def __isub__(self, other):
        if isinstance(other, Point):
            self.x -= other.x
            self.y -= other.y
        elif isinstance(other, int) or isinstance(other, float):
            self.x -= other
            self.y -= other
        else:
            raise TypeError(f"Cannot subtract type {type(other)} and Point class")

        return self

    def __mul__(self, other):
        if isinstance(other, Point):
            return Point(self.x * other.x, self.y * other.y)
        elif isinstance(other, int) or isinstance(other, float):
            return Point(self.x * other, self.y * other)
        raise TypeError(f"Cannot multiply type {type(other)} and Point class")

    def __imul__(self, other):
        if isinstance(other, Point):
            self.x *= other.x
            self.y *= other.y
        elif isinstance(other, int) or isinstance(other, float):
            self.x *= other
            self.y *= other
        else:
            raise TypeError(f"Cannot multiply type {type(other)} and Point class")

        return self

    def __truediv__(self, other):
        if isinstance(other, Point):
            if other.x != 0 and other.y != 0:
                return Point(self.x / other.x, self.y / other.y)
            raise ZeroDivisionError(f"Cannot divide by zero, Point: {other}")
        elif isinstance(other, int) or isinstance(other, float):
            if other != 0:
                return Point(self.x / other, self.y / other)
            raise ZeroDivisionError(f"Cannot divide by zero")
        raise TypeError(f"Cannot divide type {type(other)} and Point class")

    def __itruediv__(self, other):
        if isinstance(other, Point):
            if other.x != 0 and other.y != 0:
                self.x /= other.x
                self.y /= other.y
            else:
                raise ZeroDivisionError(f"Cannot divide by zero, Point: {other}")
        elif isinstance(other, int) or isinstance(other, float):
            if other != 0:
                self.x /= other
                self.y /= other
            else:
                raise ZeroDivisionError(f"Cannot divide by zero")
        else:
            raise TypeError(f"Cannot divide type {type(other)} and Point class")

        return self

    def __floordiv__(self, other):
        if isinstance(other, Point):
            if other.x != 0 and other.y != 0:
                return Point(self.x // other.x, self.y // other.y)
            raise ZeroDivisionError(f"Cannot divide by zero, Point: {other}")
        elif isinstance(other, int) or isinstance(other, float):
            if other != 0:
                return Point(self.x // other, self.y // other)
            raise ZeroDivisionError(f"Cannot divide by zero")
        raise TypeError(f"Cannot divide type {type(other)} and Point class")

    def __itruediv__(self, other):
        if isinstance(other, Point):
            if other.x != 0 and other.y != 0:
                self.x //= other.x
                self.y //= other.y
            else:
                raise ZeroDivisionError(f"Cannot divide by zero, Point: {other}")
        elif isinstance(other, int) or isinstance(other, float):
            if other != 0:
                self.x //= other
                self.y //= other
            else:
                raise ZeroDivisionError(f"Cannot divide by zero")
        else:
            raise TypeError(f"Cannot divide type {type(other)} and Point class")

        return self

    def __str__(self):
        return f"({self.x}, {self.y})"
