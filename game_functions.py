import sys
import pygame


def display_score(snake, screen):
    font = pygame.font.SysFont("arial", 30)
    score = font.render(f"Score: {snake.snake_length}", True, (0, 0, 0))
    screen.blit(score, (1000, 10))


def game_over(screen, snake, background):
    screen.blit(background, (0, 0))
    font = pygame.font.SysFont("arial", 50)
    message1 = font.render("Game Over", True, (255, 0, 0))
    message2 = font.render(f"Score: {snake.snake_length}", True, (255, 87, 51))
    message3 = font.render(
        "Press Space to start or ESC to quit", True, (0, 255, 0))
    screen.blit(message1, (550, 300))
    screen.blit(message2, (600, 400))
    screen.blit(message3, (300, 500))
    pygame.display.flip()


def check_keyDown(event, snake):
    if event.key == pygame.K_ESCAPE:
        sys.exit()
    elif event.key == pygame.K_UP and snake.snake_direction != "down":
        snake.snake_direction = "up"
    elif event.key == pygame.K_DOWN and snake.snake_direction != "up":
        snake.snake_direction = "down"
    elif event.key == pygame.K_LEFT and snake.snake_direction != "right":
        snake.snake_direction = "left"
    elif event.key == pygame.K_RIGHT and snake.snake_direction != "left":
        snake.snake_direction = "right"


def check_events(snake):
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            check_keyDown(event, snake)


def check_collisions(snake, apple):
    if pygame.Rect.colliderect(snake.rect, apple.rect):
        sound = pygame.mixer.Sound("resources/ding.mp3")
        pygame.mixer.Sound.play(sound)
        apple.move()
        snake.increase_length()


def snake_collision(snake):
    # snake head
    head_coordinates = snake.rect.topleft
    # a list of the snake's segments topleft coordinates
    segments = [(snake.x[i], snake.y[i])
                for i in range(1, snake.snake_length)]  # create a list from the second segment
    # print(segments)
    if head_coordinates in segments:
        return True
    return False


def check_edges(snake, screen):
    screen_rect = screen.get_rect()
    if snake.y[0] < 0:
        snake.y[0] = screen_rect.bottom
    elif snake.y[0] > screen_rect.bottom:
        snake.y[0] = screen_rect.top
    elif snake.x[0] < screen_rect.left:
        snake.x[0] = screen_rect.right
    elif snake.x[0] > screen_rect.right:
        snake.x[0] = screen_rect.left


def update(snake, apple, screen, background):
    screen.blit(background, (0, 0))
    snake.slither()
    apple.blit_apple()
    display_score(snake, screen)
    pygame.display.flip()
