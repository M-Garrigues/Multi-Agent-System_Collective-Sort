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

    def add_memory(self, str):
        self._mem = str + self._mem[:-1]

    def percepts(self):
        self._neighbours = self._env.get_neighbours(self.get_id())

    def move(self):
        moves = self._env.available_moves(self.get_id())
        choice = rd.randint(0, len(moves))
        self._env.move(self.get_id(), moves[choice])

    def get_id(self):
        return self._id

    def chose_action(self):
        if self._object is None:
            if [obj.has_object() for obj in self._neighbours].count(True) == 0:
                pa, pb = self.proba_neigh()
                p = rd.uniform(0, 1)
                if pa < pb:
                    square = first(self._neighbours, lambda x: x.has_object and x.get_occuppant == 'B')
                    self.add_memory('B')
                    if pb < p:
                        self._env.take_object(self, square.get_position())
                        self._object = square.get_occupant()
                else:
                    square = first(self._neighbours, lambda x: x.has_object and x.get_occuppant == 'A')
                    self.add_memory('A')
                    if pa < p:
                        self._env.take_object(self, square.get_position())
                        self._object = square.get_occupant()
            else:
                self.add_memory('0')
        else:
            if self._neighbours.is_empty is not []:
                pa, pb = self.proba_neigh()
                p = rd.uniform(0, 1)
                if pa < pb:
                    square = first(self._neighbours, lambda x: x.has_object and x.get_occuppant == 'B')
                    self.add_memory('B')
                    if pb < p:
                        self._env.put_object(self, square.get_position())
                        self._object = None
                else:
                    square = first(self._neighbours, lambda x: x.has_object and x.get_occuppant == 'A')
                    self.add_memory('A')
                    if pa < p:
                        self._env.put_object(self, square.get_position())
                        self._object = None
            else:
                self.add_memory('0')
                
    def proba_neigh(self):
        temps = self._neighbours[self._neighbours.has_object()]
        neigh = []
        for obj in temps:
            neigh.append(obj.get_occupant().get_label())
        if len(neigh) != 0:
            counts = Counter(neigh)
            if 'A' in counts:
                fa = counts['A'] / len(self._neighbours)
            else:
                fa = 0
            if 'B' in counts:
                fb = counts['B'] / len(self._neighbours)
            else:
                fb = 0
        else:
            fa = 0
            fb = 0
        if self._object is None:
            return (self._k_take / (self._k_take + fa)) ** 2, (self._k_take / (self._k_take + fb)) ** 2
        else:
            return (fa / (self._k_put + fa)) ** 2, (fb / (self._k_put + fb)) ** 2






    def is_empty(self):
        return not self._has_agent

