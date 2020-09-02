from config import *

class Weapon(object):
    def __init__(self, name, attack_speed, attack_amount):
        self.name = name
        self.attack_speed = attack_speed
        self.attack_amount = attack_amount

    def display_weapon(self):
        logger.info('Weapon Details -- Name: {} Speed: {} Attack: {}'.format(self.name, self.attack_speed, self.attack_amount))

