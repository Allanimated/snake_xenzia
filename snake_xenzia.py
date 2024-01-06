import pygame
from snake import Snake
from apple import Apple
import game_functions as gf
import time


def run_game():
    pygame.mixer.pre_init(44100, -16, 2, 1024)
    pygame.init()
    pygame.display.set_caption("Snake Xenzia")
    # game music setting
    pygame.mixer.init()
    pygame.mixer.music.load("resources/stranger_things.mp3")
    pygame.mixer.music.play(loops=-1)
    # screen setting
    screen = pygame.display.set_mode((1366, 768))
    background = pygame.image.load("resources/background.jpg")
    # Make snake
    snake = Snake(screen)
    # Make apple
    apple = Apple(screen)
    running = True
    game_over = False
    while running:

        if not game_over:
            # Event loop
            gf.check_events(snake)
            # Check snake and apple collisions
            gf.check_collisions(snake, apple)
            # Check screen edges and reset snake position
            gf.check_edges(screen=screen, snake=snake)
            # Update snake and apple movements
            gf.update(snake, apple, screen, background)
            # Check snake collision and end game
            if gf.snake_collision(snake):
                game_over = True
                pygame.mixer.music.stop()
                gf.game_over(screen, snake, background)

        if game_over:
            # handle restart and quit
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    # restart game
                    if event.key == pygame.K_SPACE:
                        game_over = False
                        pygame.mixer.music.play()
                        snake = Snake(screen)
                        apple = Apple(screen)
                    # quit game
                    elif event.key == pygame.K_ESCAPE:
                        running = False
        # delay
        time.sleep(.2)


if __name__ == "__main__":
    run_game()
