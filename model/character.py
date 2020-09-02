from config import *

class Character(object):
    def __init__(self, name, health, weapon, position):
        self.name = name
        self.health = health
        self.weapon = weapon

        self.position = position  # X,Y,Z 3D positioning

    def display_character(self):
        logger.info('A new player has joined the game! Name: {} Health: {} [Weapon: Name {} Speed: {} Attack: {}]'.format(self.name, self.health, self.weapon.name, self.weapon.attack_speed,
                                                                                                                        self.weapon.attack_amount))

