from Board import Board
from Agent import Agent


def main():
    board = Board(6, 6)
    agents = [Agent(board,'A', 1, 2, 0.3, 0.1,), Agent(board,'B', 1, 2, 0.3, 0.1), Agent(board,'C', 1, 2, 0.3, 0.1)]
    objects = [Agent(board,'4', 1, 2, 0.3, 0.1), Agent(board,'5', 1, 2, 0.3, 0.1)]
    board.init_squares(objects, agents)

    board.print()

    agents[0].move()
    agents[0].percepts()
    agents[0].chose_action()

    board.print()
    pass


if __name__ == "__main__":
    main()


