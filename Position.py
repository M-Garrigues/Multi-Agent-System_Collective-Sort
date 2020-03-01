import random as rd
from array import array


def positions_within_bounds(positions, x, y):
    ret = []
    for pos in positions:
        if x > pos.x >= 0 and y > pos.y >= 0:
            ret.append(pos)
    return ret


class Position:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Position(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Position(self.x - other.x, self.y - other.y)

    def get_neighbours(self, i):
        neighbours = []

        for x in range(-i, i + 1):
            if abs(x) == i:
                neighbours.append(Position(self.x + x, self.y))
            else:
                neighbours.append(Position(self.x + x, self.y + (i - abs(x))))
                neighbours.append(Position(self.x + x, self.y - (i - abs(x))))
        rd.shuffle(neighbours)
        return neighbours

    def print(self):
        print("("+str(self.x)+":"+str(self.y)+")")
