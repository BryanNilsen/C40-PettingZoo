# explicitly write these out
from animals import *
from attractions import *

bob = Goose("Bob", "Canada goose", "watercress sandwiches", 10123)
# bob.run()
# bob.swim()
# bob.honk()

# Create an attraction
varmint_village = PettingZoo("The Varmint Village", "critters that love to be pet!")

dolly = Llama("Dolly", "miniature llama", "morning", "hay", "#1033")
snappy = Alligator("Snappy", "American Alligator", "fish", "#1044")

varmint_village.add_animal_pythonic(dolly)
varmint_village.add_animal_type_check(dolly)
varmint_village.add_animal_pythonic(snappy)

for animal in varmint_village.animals:
    print(animal)

# Instantiate Animals
# walkers
carne_asada = Burro("Carne Asada", "Donkey", "midday", "hay", 1000)
mr_neck = Giraffe("Mr. Neck", "Masai Giraffe", "morning", "hay", 1001)
emjay = Goat("Emjay", "Mountain Goat", "evening", "grass", 1002)
dolly = Llama("Dolly", "Miniature Llama", "midday", "hay", 1003)
porkchop = Pig("Porkchop", "Pot-Bellied Pig", "morning", "corn", 1004)

# swimmers
chompy = Alligator("Chompy", "American Alligator", "chicken", 1005)
quackers = Duck("Quackers", "Mallard", "fish", 1006)
finley = Fish("Finley", "Koi", "worms", 1007)
whiskers = Otter("Whiskers", "River Otter", "fish", 1008)
mitch = Turtle("Mitch", "Tortoise", "lettuce", 1009)

# slitherers
elizardbeth = Lizard("Elizardbeth", "Gecko", "crickets", 1010)
donald = Slug("Donald", "Disgusting Slug", "lettuce", 1011)
shelly = Snail("Shelly", "Garden Snail", "lettuce", 1012)
lindsey = Snake("Lindsey", "Ratsnake", "mice", 1013)
slippy = Worm("Slippy", "Earthworm", "grass", 1014)


# Instantiate Attractions
friendly_farm = PettingZoo("Friendly Farm", "cute and fuzzy critters to cuddle")
slitherland = SnakePit("Slither Land", "sleek, slithering critters to give you the creepy crawlies")
critter_creek = Wetlands("Critter Creek", "swimming and splashing critters to smile at")

# Admit Animals to Attraction
# Friendly Farm
friendly_farm.add_animal(dolly)
friendly_farm.add_animal(carne_asada)
friendly_farm.add_animal(mr_neck)
friendly_farm.add_animal(emjay)
friendly_farm.add_animal(porkchop)
# Slitherland
slitherland.add_animal(elizardbeth)
slitherland.add_animal(donald)
slitherland.add_animal(shelly)
slitherland.add_animal(slippy)
slitherland.add_animal(lindsey)
# Critter Creek
critter_creek.add_animal(chompy)
critter_creek.add_animal(quackers)
critter_creek.add_animal(finley)
critter_creek.add_animal(whiskers)
critter_creek.add_animal(mitch)


def attraction_animals_report(*attractions):
    '''  
    Print a report of all animals in each attraction
    Arguments:
    *args = accepts any number of attraction objects
    '''
    print('::: ATTRACTION ANIMAL REPORT :::')
    print('')
    for attraction in attractions:
        print(f'{attraction}')
        for animal in attraction.animals:
            print(f' . {animal.name} - {animal.species}')
        print('')


# PRINT STATEMENTS
# Print Report
# attraction_animals_report(friendly_farm, slitherland, critter_creek)

# print(friendly_farm)

# print("Friendly Farm's Newest Animal is", friendly_farm.last_critter_added)
