from Position import Position
from Square import Square
from numpy import random as rand


class Board:

    def __init__(self, n, m, agents, objects):
        self._squares = [[Square() for _ in range(m)] for _ in range(n)]  # initialises a m*n board of squares
        self._agents = agents
        self._objects = objects

        self.init_squares()
        self.place_occupants(objects, agents)

    ##### INIT #####

    def init_squares(self):
        for x in range(len(self._squares)):
            for y in range(len(self._squares[0])):
                self._squares[x][y].set_position(Position(x, y))

    def place_occupants(self, objects, agents):
        assert (len(objects) + len(agents) < len(self._squares) * len(self._squares[0]))

        m = len(self._squares)
        n = len(self._squares[0])
        len_obj = len(objects)

        shuffled = rand.permutation(m*n)

        for i in range(len_obj):
            pos = Position(shuffled[i] % m, int(shuffled[i] / m))
            self._squares[pos.x][pos.y].set_occupant(objects[i])

        for i in range(len_obj, len(agents) + len_obj):
            pos = Position(shuffled[i] % m, int(shuffled[i] / m))
            self._squares[pos.x][pos.y].set_occupant(agents[i - len_obj])

    ##### PERCEPTION #####

    def available_moves(self, agent):
        return

    ##### MOVES #####

    def move(self, agent, direction):
        return

    ##### ACTIONS #####

    def take_object(self, agent):
        pos = self._agent_positions[agent.get_id()]

    def print(self):
        for row in self._squares:
            line = "|"
            for square in row:
                line += square.to_string()
                line += "|"

            print(line)
