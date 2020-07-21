from .attraction import Attraction


class SnakePit(Attraction):

    def __init__(self, name, description):
        super().__init__(name, description)
    # Number 1: Duck typing check
    def add_animal_pythonic(self, animal):
        try:
            if animal.slither_speed > -1:
                self.animals.append(animal)
        except AttributeError as ex:
            print(f'{animal} doesn\'t like to be with slithery critters, so please do not put it in the {self.name} attraction.')

    # Number 2: Actual typing check
    def add_animal_type_check(self, animal):
        if isinstance(animal, Slithering):
            self.animals.add(animal)
        else:
            print(f'{animal} doesn\'t like to be slithery critters, so please do not try to put it in the {self.name} attraction.')