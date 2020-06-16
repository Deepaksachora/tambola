import random

games = {}


class Game:
    def __init__(self):
        self._id = random.randint(100, 999)

    def get_id(self):
        return self._id
