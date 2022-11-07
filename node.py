from typing import Union


class Node(object):
    def __init__(self, weight: Union[int, float] = 0, label: str = ""):

        if not isinstance(weight, int) and not isinstance(weight, float):
            raise TypeError("weight must be an integer or float")

        if not isinstance(label, str):
            raise TypeError("label must be a string")

        self.weight = weight
        self.label = label

    def change_weight(self, weight: int):

        if not isinstance(weight, int) and not isinstance(weight, float):
            raise TypeError("weight must be an integer or float")

        self.weight = weight

    def __str__(self):
        if self.label:
            return f"Node {self.label}: {self.weight}"
        else:
            return f"Node: {self.weight}"
