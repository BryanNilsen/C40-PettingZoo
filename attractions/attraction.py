class Attraction:

    def __init__(self, name):
        self.attraction_name = name
        self.animals = list()

    @property
    def last_critter_added(self):
        return (f'{self.animals[-1].name} the {self.animals[-1].species}')

    def admit_animal(self, animal):
        self.animals.append(animal)

    def __str__(self):
        return f"{self.attraction_name} is a place where you will find {self.description}"
