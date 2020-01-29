from Position import Position, positions_within_bounds
from Square import Square
from numpy import random as rand


class Board:

    def __init__(self, n, m):
        self._squares = [[Square() for _ in range(m)] for _ in range(n)]  # initialises a m*n board of squares
        self._n = n
        self._m = m
        self._agents = None
        self._objects = None
        self._agents_positions = {}

    ##### INIT #####

    def init_squares(self, objects, agents):
        for x in range(len(self._squares)):
            for y in range(len(self._squares[0])):
                self._squares[x][y].set_position(Position(x, y))
        self.place_occupants(objects, agents)

    def place_occupants(self, objects, agents):
        assert (len(objects) + len(agents) < len(self._squares) * len(self._squares[0]))

        self._agents = agents
        self._objects = objects

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
            self._agents_positions[agents[i - len_obj].get_id()] = pos

    ##### PERCEPTION #####

    def perceive(self, agent):
        pos = self._agents_positions[agent.get_id()]
        visibles = positions_within_bounds(pos.get_neighbours(agent._i), self._m, self._n)

        squares = []
        for position in visibles:
            squares.append(self._squares[pos.x][pos.y])
        return squares

    def available_moves(self, agent):
        return

    ##### MOVES #####

    def move(self, agent, direction):
        agent_pos = self._agents_positions[agent.get_id()]
        step = agent._i

        if direction == 'N':
            newpos = agent_pos - Position(step, 0)
        elif direction == 'S':
            newpos = agent_pos + Position(step, 0)
        elif direction == 'E':
            newpos = agent_pos + Position(0, step)
        else:
            newpos = agent_pos - Position(0, step)

        self._agents_positions[agent.get_id()] = newpos

        return newpos

    ##### ACTIONS #####

    def take_object(self, agent):
        pos = self._agents_positions[agent.get_id()]

    def print(self):
        for row in self._squares:
            line = "|"
            for square in row:
                line += square.to_string()
                line += "|"

            print(line)
