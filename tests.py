import random
import string

def randomizer():
    numerics = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    
    alphabets = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", 
    "N" ,"O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

    ranchoices = (random.choices(alphabets, k = 10))

    print(ranchoices)

randomizer()

# def randomizer2(length = 10, uppercase = True, numbers = True):
#     character_set = ""

#     return "".join(random.choice(character_set))

# randomis = randomizer2(10)
# print(randomis)
