import logging
import arcade

from .constants import SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE
from .game import MyGame

if __name__ == "__main__":
    logging.basicConfig(
        level=logging.DEBUG,
        handlers=[logging.StreamHandler()],
         format="%(name)s [%(levelname)s] (%(filename)s @ %(lineno)d) %(message)s")

    logging.getLogger("arcade.application").setLevel(logging.INFO)

    game = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    game.setup()
    arcade.run()
