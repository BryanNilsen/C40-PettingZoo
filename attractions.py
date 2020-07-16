

class PettingZoo:

    def __init__(self, name):
        self.attraction_name = name
        self.description = "cute and fuzzy critters to cuddle"
        self.animals = list()

    @property
    def last_critter_added(self):
        return (f'{self.animals[-1].name} the {self.animals[-1].species}')

    def admit_animal(self, animal):
        self.animals.append(animal)
        # print(f'You have admitted {animal.name} the {animal.species}')

    def __str__(self):
        return f"{self.attraction_name} is a place where you will find {self.description}"


class SnakePit:

    def __init__(self, name):
        self.attraction_name = name
        self.description = "sleek, slithering critters to give you the creepy crawlies"
        self.animals = list()

    @property
    def last_critter_added(self):
        return (f'{self.animals[-1].name} the {self.animals[-1].species}')

    def admit_animal(self, animal):
        self.animals.append(animal)
        # print(f'You have admitted {animal.name} the {animal.species}')

    def __str__(self):
        return f"{self.attraction_name} is a place where you will find {self.description}"


class Wetlands:

    def __init__(self, name):
        self.attraction_name = name
        self.description = "swimming and splashing critters to smile at"
        self.animals = list()

    @property
    def last_critter_added(self):
        return (f'{self.animals[-1].name} the {self.animals[-1].species}')

    def admit_animal(self, animal):
        self.animals.append(animal)
        # print(f'You have admitted {animal.name} the {animal.species}')

    def __str__(self):
        return f"{self.attraction_name} is a place where you will find {self.description}"
