from .attraction import Attraction


class SnakePit(Attraction):

    def __init__(self, name):
        super().__init__(name)
        self.description = "sleek, slithering critters to give you the creepy crawlies"
