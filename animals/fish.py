from .animal import Animal
from movements import Swimming

class Fish(Animal):
    def __init__(self, name, species, food, chip_num):
        Animal.__init__(self, name, species, food, chip_num)
        Swimming.__init__(self)

    def __str__(self):
        return f'{self.name} the fish'