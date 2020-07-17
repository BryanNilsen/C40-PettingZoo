from .attraction import Attraction


class Wetlands(Attraction):

    def __init__(self, name):
        super().__init__(name)
        self.description = "swimming and splashing critters to smile at"
