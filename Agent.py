import random as rd
from statistics import mode
from collections import Counter


class Agent:

    def __init__(self, env, id, t, i, k_take, k_put):
        self._env = env
        self._t = t
        self._i = i
        self._mem = "0" * t
        self._neighbours = None
        self._id = id
        self._object = None
        self._type = "Agent"
        self._k_take = k_take
        self._k_put = k_put

    def add_memory(self, obj):
        self._mem = obj.get_type() + self._mem[:-1]

    def percepts(self):
        self._neighbours = self._env.get_neighbours(self.get_id())

    def move(self):
        moves = self._env.get_possible_moves(self.get_id())
        choice = rd.randint(0, len(moves))
        self._env.move(self.get_id(), moves[choice], self._i)

    def get_id(self):
        return self._id

    def chose_action(self):
        for obj in self._neighbours:
            neigh.append(obj.get_type())
        temps = self._neighbours[neigh == "A" or neigh == "B"]
        neigh = neigh[neigh == "A" or neigh == "B"]

    def proba_neigh(self):
        temps = self._neighbours[self._neighbours.has_object()]
        neigh = []
        for obj in temps:
            neigh.append(obj.get_occupant().get_type())
        if len(neigh) != 0:
            counts = Counter(neigh)
            if counts.has_key('A'):
                fa = counts['A']/len(self._neighbours)
            else:
                fa = 0
            if counts.has_key('B'):
                fb = counts['B']/len(self._neighbours)
            else:
                fb = 0
        else:
            fa = 0
            fb = 0
        if self._object is None:
            return (self._k_take/(self._k_take + fa))**2, (self._k_take/(self._k_take + fb))**2
        else:
            return (fa / (self._k_put + fa)) ** 2, (fb / (self._k_put + fb)) ** 2
