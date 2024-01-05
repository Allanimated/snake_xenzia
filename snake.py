import pygame

SIZE = 40


class Snake:
    def __init__(self, screen) -> None:
        self.screen = screen
        self.block = pygame.image.load("resources/block.jpg").convert()
        self.rect = self.block.get_rect()
        # Snake dimensions
        self.snake_size = 40
        self.snake_length = 5
        self.x = [40] * self.snake_length
        self.y = [40] * self.snake_length
        # snake movement
        self.snake_direction = "down"

    def update_body(self):
        # update body
        for i in range((self.snake_length - 1), 0, -1):
            self.x[i] = self.x[i-1]
            self.y[i] = self.y[i-1]

    def update_head(self):
        # update head
        if self.snake_direction == "up":
            self.y[0] -= SIZE
        elif self.snake_direction == "down":
            self.y[0] += SIZE
        elif self.snake_direction == "left":
            self.x[0] -= SIZE
        elif self.snake_direction == "right":
            self.x[0] += SIZE

        # Update the rect attribute to the new head position
        self.rect.topleft = (self.x[0], self.y[0])

    def slither(self):
        self.update_body()
        self.update_head()
        # draw snake after every update
        self.blit_snake()

    def increase_length(self):
        self.snake_length += 1
        self.x.append(40)
        self.y.append(40)

    def blit_snake(self):
        for i in range(self.snake_length):
            self.screen.blit(self.block, (self.x[i], self.y[i]))


# screen = pygame.display.set_mode((1366, 768))
# screen_rect = screen.get_rect()
# snake = Snake(screen)
# snake.increase_length()
# snake.increase_length()
# print(screen_rect.left)
# print(screen_rect.right)
