from Board import Board
from Position import Position, positions_within_bounds
from temp import Agent


def main():
    agents = [Agent('A'), Agent('B'), Agent('C')]
    objects = [Agent('4'), Agent('5'), Agent('6'), Agent('7'), Agent('8')]
    board = Board(6, 6, agents, objects)

    board.print()


    pass


if __name__ == "__main__":
    main()


