from Board import Board
from Position import Position, positions_within_bounds


def main():
    agents = []
    objects = []
    #board = Board(10, 10, agents, objects)

    #board.print()

    point = Position(1, 1)
    point.print()

    neig = point.get_neighbours(2)
    for p in neig:
        p.print()

    valid = positions_within_bounds(neig, 4, 4)
    for v in valid:
        v.print()

    pass


if __name__ == "__main__":
    main()


