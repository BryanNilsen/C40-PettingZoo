

class PettingZoo:

    def __init__(self, name):
        self.attraction_name = name
        self.description = "cute and fuzzy critters to cuddle"
        self.animals = list()

    def admit_animal(self, animal):
        self.animals.append(animal)
        # print(f'You have admitted {animal.name} the {animal.species}')


class SnakePit:

    def __init__(self, name):
        self.attraction_name = name
        self.description = "sleek, slithering critters to give you the creepy crawlies"
        self.animals = list()

    def admit_animal(self, animal):
        self.animals.append(animal)
        # print(f'You have admitted {animal.name} the {animal.species}')


class Wetlands:

    def __init__(self, name):
        self.attraction_name = name
        self.description = "swimming and splashing critters to smile at"
        self.animals = list()

    def admit_animal(self, animal):
        self.animals.append(animal)
        # print(f'You have admitted {animal.name} the {animal.species}')
