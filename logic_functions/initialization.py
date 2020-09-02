import math
import string
import random
from model.character import Character
from model.weapon import Weapon


def build_random_character():
    letters = string.ascii_lowercase
    player_name_str = ''.join(random.choice(letters) for i in range(8))
    weapon_name_str = ''.join(random.choice(letters) for i in range(4))

    weapon = Weapon('weapon_' + weapon_name_str, random.randint(1, 10), random.randint(1, 10))

    return Character('player_' + player_name_str,  random.randint(10, 100), weapon, (random.randrange(0, 10), random.randrange(0, 10), random.randrange(0, 10)))

