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

    def get_label(self):
        return self._id

    def add_memory(self, str):
        self._mem = str + self._mem[:-1]

    def percepts(self):
        self._neighbours = self._env.perceive(self)

    def move(self):
        moves = self._env.available_moves(self)
        if len(moves) != 0:
            choice = rd.randint(0, len(moves) - 1)
            self._env.move(self, moves[choice])

    def get_id(self):
        return self._id

    def chose_action(self):
        if self._object is None:
            if [obj.has_object() for obj in self._neighbours].count(True) != 0:
                pa, pb = self.proba_mem(0.2)
                p = rd.uniform(0, 1)
                print(self._id)
                print(pa, pb)
                if pa < pb and "B" in [obj.get_occupant().get_label() for obj in self._neighbours if obj.has_object()]:
                    square = next(
                        obj for obj in self._neighbours if obj.has_object() and obj.get_occupant().get_label() == 'B')
                    self.add_memory('B')
                    if pb < p:
                        self._object = square.get_occupant()
                        self._env.take_object(square)
                elif "A" in [obj.get_occupant().get_label() for obj in self._neighbours if obj.has_object()]:
                    square = next(
                        obj for obj in self._neighbours if obj.has_object() and obj.get_occupant().get_label() == 'A')
                    self.add_memory('A')
                    if pa < p:
                        self._object = square.get_occupant()
                        self._env.take_object(square)
            else:
                self.add_memory('0')
        else:
            if [obj.is_empty() for obj in self._neighbours].count(True) != 0:
                pa, pb = self.proba_neigh()
                p = rd.uniform(0, 1)
                if self._object.get_label() == 'B':
                    square = next(obj for obj in self._neighbours if obj.is_empty())
                    self.add_memory('B')
                    if pb < p:
                        self._env.put_object(self, square)
                        self._object = None
                else:
                    square = next(obj for obj in self._neighbours if obj.is_empty())
                    self.add_memory('A')
                    if pa < p:
                        self._env.put_object(self, square)
                        self._object = None
            else:
                self.add_memory('0')

    def proba_neigh(self):
        temps = [obj for obj in self._neighbours if obj.has_object()]
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

    def proba_mem(self, e):

        fa = (self._mem.count("A") + e * self._mem.count("B"))/len(self._mem)
        fb = (self._mem.count("B") + e * self._mem.count("A"))/len(self._mem)
        temps = [obj for obj in self._neighbours if obj.has_object()]
        neigh = []
        for obj in temps:
            neigh.append(obj.get_occupant().get_label())
        if len(neigh) != 0:
            counts = Counter(neigh)
            if 'A' not in counts:
                fa = 0
            if 'B' not in counts:
                fb = 0
        else:
            fa = 0
            fb = 0
        if self._object is None:
            return (self._k_take / (self._k_take + fa)) ** 2, (self._k_take / (self._k_take + fb)) ** 2
        else:
            return (fa / (self._k_put + fa)) ** 2, (fb / (self._k_put + fb)) ** 2


    def print(self):
        print("Agent : ", self._id)
        if self._object is None:
            print("Object held : ", self._object)
        else:
            print("Object held : ", self._object.get_label())
        print("Memory : ", self._mem)
