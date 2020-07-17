from .attraction import Attraction


class PettingZoo(Attraction):

    def __init__(self, name):
        super().__init__(name)
        self.description = "cute and fuzzy critters to cuddle"
