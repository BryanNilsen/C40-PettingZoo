from animals import *
from attractions import *

# Instantiate Animals
# walkers
carne_asada = Burro("Carne Asada", "Donkey", "midday")
mr_neck = Giraffe("Mr. Neck", "Masai Giraffe", "morning")
emjay = Goat("Emjay", "Mountain Goat", "evening")
dolly = Llama("Dolly", "Miniature Llama", "midday")
porkchop = Pig("Porkchop", "Pot-Bellied Pig", "morning")

# swimmers
chompy = Alligator("Chompy", "American Alligator")
quackers = Duck("Quackers", "Mallard")
finley = Fish("Finley", "Koi")
whiskers = Otter("Whiskers", "River Otter")
mitch = Turtle("Mitch", "Tortoise")

# slitherers
elizardbeth = Lizard("Elizardbeth", "Gecko")
donald = Slug("Donald", "Disgusting Slug")
shelly = Snail("Shelly", "Garden Snail")
lindsey = Snake("Lindsey", "Ratsnake")
slippy = Worm("Slippy", "Earthworm")


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
slitherland.admit_animal(elizardbeth)
slitherland.admit_animal(donald)
slitherland.admit_animal(shelly)
slitherland.admit_animal(slippy)
slitherland.admit_animal(lindsey)
# Critter Creek
critter_creek.admit_animal(chompy)
critter_creek.admit_animal(quackers)
critter_creek.admit_animal(finley)
critter_creek.admit_animal(whiskers)
critter_creek.admit_animal(mitch)


#
def attraction_animals_report(*attractions):
    '''  
    Print a report of all animals in each attraction
    Arguments:
    *args = accepts any number of attraction objects
    '''
    print('::: ATTRACTION ANIMAL REPORT :::')
    print('')
    for attraction in attractions:
        print(
            f'{attraction.attraction_name} is where you will find {attraction.description}')
        for animal in attraction.animals:
            print(f' . {animal.name} - {animal.species}')
        print('')


# Print Report
attraction_animals_report(friendly_farm, slitherland, critter_creek)
