class Square:

    def __init__(self):
        self._has_agent = False
        self._has_object = False
        self._agent = None
        self._object = None

    def has_agent(self):
        return self._has_agent

    def has_object(self):
        return self._has_object

    def get_object(self):
        return self._object

    def get_agent(self):
        return self._agent

    def set_object(self, object):
        assert (not self._has_object)
        self._object = object
        self._has_object = True

    def set_agent(self, agent):
        assert (not self._has_agent)
        self._agent = agent
        self._has_agent = True

    def take_object(self):
        temp_object = self._object
        self._object = None
        self._has_object = False
        return temp_object

    def take_agent(self):
        temp_agent = self._object
        self._agent = None
        self._has_agent = False
        return temp_agent

    def to_string(self):
        string = ""

        if self._has_object:
            string += self._object.label
        if self._has_agent:
            string += self._agent.id
        while len(string) < 2:
            string += "-"

        print(string)
