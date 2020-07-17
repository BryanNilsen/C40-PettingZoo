# explicitly write these out
from animals import *
from attractions import *

bob = Goose("Bob", "Canada goose", "watercress sandwiches", 10123)
bob.run()
bob.swim()
bob.honk()


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
friendly_farm = PettingZoo("Friendly Farm")
slitherland = SnakePit("Slither Land")
critter_creek = Wetlands("Critter Creek")

# Admit Animals to Attraction
# Friendly Farm
friendly_farm.admit_animal(dolly)
friendly_farm.admit_animal(carne_asada)
friendly_farm.admit_animal(mr_neck)
friendly_farm.admit_animal(emjay)
friendly_farm.admit_animal(porkchop)
# Slitherland
# slitherland.admit_animal(elizardbeth)
# slitherland.admit_animal(donald)
slitherland.admit_animal(shelly)
slitherland.admit_animal(slippy)
slitherland.admit_animal(lindsey)
# Critter Creek
critter_creek.admit_animal(chompy)
critter_creek.admit_animal(quackers)
critter_creek.admit_animal(finley)
critter_creek.admit_animal(whiskers)
critter_creek.admit_animal(mitch)


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
attraction_animals_report(friendly_farm, slitherland, critter_creek)

print(friendly_farm)

print("Friendly Farm's Newest Animal is", friendly_farm.last_critter_added)
