from config import *
import sys, random, math

class GameBoard(object):
    def __init__(self, attack_duration):
        self.character_list = []
        self.attack_duration = attack_duration
        self.matrix = None  # TODO This is where we would have a 3D matrix for distance calculation
        self.state = None  # TODO we can have a state here later

    def add_character_to_board(self, character):
        logger.info('Adding Character {} to game board'.format(character.name))
        self.character_list.append(character)

    def delete_character_to_board(self, character):
        logger.info('Character {} Died! Removing from game.'.format(character.name))
        self.character_list.remove(character)
        if len(self.character_list) == 1:
            logger.info('GAME OVER!!!  {} WINS!'.format(self.character_list[0].name))
            sys.exit(1)

    def attack_move(self):
        attacker = random.choice(self.character_list)
        defender = random.choice(self.character_list)
        if attacker is defender:
            return   # Why beat up on yourself?

        strike = self.attack_duration
        while True:
            if strike > attacker.weapon.attack_speed:
                logger.info('Character {} attacked {}!!'.format(attacker.name, defender.name))
                defender.health = defender.health - attacker.weapon.attack_amount
                logger.info('Defender {} has {} health left!'.format(defender.name, defender.health))
                if defender.health < 0:
                    self.delete_character_to_board(defender)
                    return
                strike = strike - attacker.weapon.attack_speed
            else:
                # Not enough time for a strike
                return

    def print_board(self):
        logger.info('The characters left on the board are:')

    # TODO Euclidean distance from attacker to defender:
    def calculate_strike_distance(self, attacker, defender):
        distance = math.sqrt(sum([(a - b) ** 2 for a, b in zip(attacker.position, defender.position)]))
        logger.info("Distance from attacker to defender is: ", distance)
