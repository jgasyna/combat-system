from config import *
from model.character import Character
from model.game_board import GameBoard
from logic_functions.initialization import *
import time


if __name__ == "__main__":
    logging.info('<--------- STARTING COMBAT SYSTEM PLAY -------- >')
    logging.info('Initializing characters....')



    character_a = build_random_character()
    character_a.display_character()
    character_b = build_random_character()
    character_b.display_character()
    character_c = build_random_character()
    character_c.display_character()

    logging.info('Initializing characters....Setting Attack duration to 10')
    board = GameBoard(10)
    board.add_character_to_board(character_a)
    board.add_character_to_board(character_b)
    board.add_character_to_board(character_c)

    while True:
        board.attack_move()
        time.sleep(1)


