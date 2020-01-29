from Square import Square


class Board:

    def __init__(self, n, m, agents, objects):
        self._squares = [[Square()] * m for _ in range(n)]  # initialises a m*n board of squares
        self._agents = agents
        self._objects = objects

    ##### INIT #####

    def init_squares(self):

        for x in range(len(self._squares)):
            for y in 
        return

    def place_objects(self, objects):
        return

    def place_agents(self, agents):
        return

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
