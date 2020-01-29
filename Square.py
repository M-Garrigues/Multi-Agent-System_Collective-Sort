class Square:

    def __init__(self):
        self._has_agent = False
        self._has_object = False
        self._occupant = None

    def has_agent(self):
        return self._has_agent

    def has_object(self):
        return self._has_object

    def get_occupant(self):
        return self._occupant

    def set_occupant(self, occupant):
        assert (not self._has_object and not self._has_agent)

        self._occupant = occupant
        if type(occupant).__name__ == "Agent":
            self._has_agent = True
        else:
            self._has_object = True

    def take_occupant(self):
        temp_occupant = self._occupant
        self._occupant = None
        self._has_agent = False
        self._has_object = False
        return temp_occupant

    def to_string(self):
        if self._has_object:
            print(self._occupant.label)
        elif self._has_agent:
            print(self._occupant.id)
        else:
            print("-")