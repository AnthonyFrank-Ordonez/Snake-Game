from collections import namedtuple


Colour = namedtuple("Colour", ["red", "green", "blue"])
BG = Colour(red=0, green=0, blue=0)
PLAY_BG = Colour(red=0, green=0, blue=0)
SNAKE_TITLE = Colour(red=255, green=255, blue=255)
PLAY_TITLE = Colour(red=255, green=255, blue=255)
SCORE = Colour(red=255, green=255, blue=255)
FOOD_COLOR = Colour(red=255, green=253, blue=65)
SNAKE_COLOR = Colour(red=255, green=255, blue=255)
GAME_OVER = Colour(red=255, green=255, blue=255)