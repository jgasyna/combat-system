from config import *

class Character(object):
    def __init__(self, name, health, weapon):
        self.name = name
        self.health = health
        self.weapon = weapon
        # TODO Have a Tuple of X,Y,Z 3D positioning
        self.position = None

    def display_character(self):
        logger.info('A new player has joined the game! Name: {} Health: {} Weapon: Name {} Speed: {} Attack: {}'.format(self.name, self.health, self.weapon.name, self.weapon.attack_speed,
                                                                                                                        self.weapon.attack_amount))

