from datetime import date


#  WALKING ANIMALS

class Llama():
    def __init__(self, name, species, shift):
        # Establish the properties of each animal
        # with a default value
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.shift = shift
        self.walking = True


class Giraffe():
    def __init__(self, name, species, shift):
        # Establish the properties of each animal
        # with a default value
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.shift = shift
        self.walking = True


class Goat():
    def __init__(self, name, species, shift):
        # Establish the properties of each animal
        # with a default value
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.shift = shift
        self.walking = True


class Burro():
    def __init__(self, name, species, shift):
        # Establish the properties of each animal
        # with a default value
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.shift = shift
        self.walking = True


class Pig():
    def __init__(self, name, species, shift):
        # Establish the properties of each animal
        # with a default value
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.shift = shift
        self.walking = True


#  SWIMMING ANIMALS

class Otter():
    def __init__(self, name, species):
        # Establish the properties of each animal
        # with a default value
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.swimming = True


class Fish():
    def __init__(self, name, species):
        # Establish the properties of each animal
        # with a default value
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.swimming = True


class Duck():
    def __init__(self, name, species):
        # Establish the properties of each animal
        # with a default value
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.swimming = True


class Alligator():
    def __init__(self, name, species):
        # Establish the properties of each animal
        # with a default value
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.swimming = True


class Turtle():
    def __init__(self, name, species):
        # Establish the properties of each animal
        # with a default value
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.swimming = True

#  SLITHERING ANIMALS


class Snake():
    def __init__(self, name, species):
        # Establish the properties of each animal
        # with a default value
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.slithering = True


class Snail():
    def __init__(self, name, species):
        # Establish the properties of each animal
        # with a default value
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.slithering = True


class Worm():
    def __init__(self, name, species):
        # Establish the properties of each animal
        # with a default value
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.slithering = True


class Slug():
    def __init__(self, name, species):
        # Establish the properties of each animal
        # with a default value
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.slithering = True


class Lizard():
    def __init__(self, name, species):
        # Establish the properties of each animal
        # with a default value
        self.name = name
        self.name = species
        self.date_added = date.today()
        self.slithering = True


# Make instances of each
chompy = Alligator("Chompy", "American Alligator")
carne_asada = Burro("Carne Asada", "Donkey", "midday")
quackers = Duck("Quackers", "Mallard")
finley = Fish("Finley", "Koi")
mr_neck = Giraffe("Mr. Neck", "Masai Giraffe", "morning")
emjay = Goat("Emjay", "Mountain Goat", "evening")
elizardbeth = Lizard("Elizardbeth", "Gecko")
dolly = Llama("Dolly", "Miniature Llama", "midday")
whiskers = Otter("Whiskers", "River Otter")
porkchop = Pig("Porkchop", "Pot-Bellied Pig", "morning")
donald = Slug("Donald", "Disgusting Slug")
shelly = Snail("Shelly", "Garden Snail")
lindsey = Snake("Lindsey", "Ratsnake")
mitch = Turtle("Mitch", "Tortoise")
slippy = Worm("Slippy", "Earthworm")


print(f'{dolly.name} the {dolly.species} is available to pet during the {dolly.shift} shift.')
