class Square:

    def __init__(self):
        self._has_agent = False
        self._has_object = False
        self._occupant = None
        self._position = None

    def get_position(self):
        return self._position

    def set_position(self, position):
        self._position = position

    def has_agent(self):
        return self._has_agent

    def has_object(self):
        return self._has_object

    def is_empty(self):
        return not (self._has_agent or self._has_object)

    def get_occupant(self):
        return self._occupant

    def set_occupant(self, occupant):
        if type(occupant).__name__ == "Agent":
            assert (not self._has_agent)
            self._has_agent = True
        elif type(occupant).__name__ == "Objects":
            assert (not self._has_object)
            self._has_object = True
        else:
            assert False  # Set occupant, while occupant has wrong class
        self._occupant = occupant

    def take_occupant(self):
        temp_occupant = self._occupant
        self._occupant = None
        self._has_agent = False
        self._has_object = False
        return temp_occupant

    def to_string(self):
        if self._has_object:
            return self._occupant.get_label()
        elif self._has_agent:
            return self._occupant.get_id()
        else:
            return '-'
