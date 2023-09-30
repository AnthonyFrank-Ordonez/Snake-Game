import time
import pygame
from data_files.game_settings import *
from data_files.new_cl import BG, PLAY_BG, SNAKE_TITLE, PLAY_TITLE, SCORE, FOOD_COLOR, SNAKE_COLOR, GAME_OVER
from random import randint


def wall_collision():
    """Collision function that will check if the snake have hit the wall or its body"""
    x, y = SNAKE_POST[0]

    return (
        x in (-20, WINDOW_WIDTH)
        or y in (20, WINDOW_HEIGHT)
        or (x, y) in SNAKE_POST[1:]
    )


def food_collision(food_post):  # food collision function
    """Food Collision function that will check if the position of the snake is in the food position"""
    if SNAKE_POST[0] == food_post:
        SNAKE_POST.append(SNAKE_POST[-1])
        return True


def move_snake(current_direct):
    """function for the keys to move the snake"""
    x, y = SNAKE_POST[0]

    if current_direct == "Left":
        new_head_post = (x - SEGMENT_SIZE, y)

    elif current_direct == "Right":
        new_head_post = (x + SEGMENT_SIZE, y)

    elif current_direct == "Down":
        new_head_post = (x, y + SEGMENT_SIZE)

    elif current_direct == "Up":
        new_head_post = (x, y - SEGMENT_SIZE)

    SNAKE_POST.insert(0, new_head_post)
    del SNAKE_POST[-1]


def on_arrow_press(event, current_direct):
    """function to read if the keys press to move the snake is valid"""
    key = event.__dict__["key"]
    new_direction = KEY_MAP.get(key)

    all_direction = ["Right", "Left", "Up", "Down"]
    opposite_direction = [{"Right", "Left"}, {"Up", "Down"}]

    if new_direction in all_direction and {new_direction, current_direct} not in opposite_direction:
        return new_direction

    return current_direct


def draw_obj(screen, food_post):
    """Function to draw the snake and the food object"""
    pygame.draw.rect(screen, FOOD_COLOR, [food_post, (SEGMENT_SIZE, SEGMENT_SIZE)])

    for x, y in SNAKE_POST:
        pygame.draw.rect(screen, SNAKE_COLOR, [x, y, SEGMENT_SIZE, SEGMENT_SIZE])


def set_food_post():  # function to set the location of the food
    """Set the Food position of the snake"""
    while True:
        x = randint(0, 39) * SEGMENT_SIZE
        y = randint(2, 41) * SEGMENT_SIZE

        food_post = (x, y)

        if food_post not in SNAKE_POST and x < WINDOW_WIDTH and y < WINDOW_HEIGHT:
            return food_post


def play(clock, screen, current_direct, score):
    """Play Function of the Snake Game"""
    food_post = set_food_post()  # set the location of the food
    pygame.display.set_caption("Snake Game")  # play caption

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

            elif event.type == pygame.KEYDOWN:
                current_direct = on_arrow_press(event, current_direct)

        screen.fill(PLAY_BG)
        draw_obj(screen, food_post)  # draw the snake and food

        # score font
        score_font = pygame.font.Font(None, 28)
        score_title = score_font.render(f"Score: {score}", True, SCORE)
        screen.blit(score_title, [570, 10])

        pygame.display.update()

        move_snake(current_direct)  # move the snake

        if wall_collision():
            # font for game over
            game_over = pygame.font.SysFont("Just My Type", 150)
            game_over_title = game_over.render("Game Over", True, GAME_OVER)
            screen.blit(game_over_title, [110, 210])

            pygame.display.update()

            time.sleep(2)  # wait 2 secs to exit the game

            return

        if food_collision(food_post):
            food_post = set_food_post()
            score += 1

        clock.tick(15)


# Main Menu Function
def main(start):
    """Main function"""
    pygame.display.set_caption("MAIN MENU")  # set caption
    clock = pygame.time.Clock()  # fps
    SCREEN = pygame.display.set_mode(DIMENSION)

    while start is False:  # Main Menu
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

            if event.type == pygame.KEYDOWN:
                if event.key == 32:
                    start = True

        SCREEN.fill(BG)

        # title
        title_font = pygame.font.SysFont("Just My Type", 150)
        snake_title = title_font.render("Snake Game", True, SNAKE_TITLE)
        SCREEN.blit(snake_title, [85, 210])

        # Press space to play
        play_font = pygame.font.SysFont("Arial", 30)
        play_title = play_font.render("Press 'space' to play", True, PLAY_TITLE)
        SCREEN.blit(play_title, [230, 410])

        pygame.display.update()

    else:
        play(clock, SCREEN, CURRENT_DIRECTION, PLAYER_SCORE)


if __name__ == '__main__':
    """initialize pygame and font"""
    pygame.init()
    pygame.font.init()
    main(START)