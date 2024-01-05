import pygame
import random


class Apple:
    def __init__(self, screen) -> None:
        self.apple = pygame.image.load("resources/apple.jpg").convert()
        self.screen = screen
        self.screen_rect = self.screen.get_rect()
        self.rect = self.apple.get_rect()
        self.x = 683
        self.y = 384
        self.rect.x = self.x
        self.rect.y = self.y

    def move(self):
        # move apple at random positions
        self.x = random.randint(1, (self.screen_rect.width - 60) // 40) * 40
        self.y = random.randint(1, (self.screen_rect.height - 60) // 40) * 40
        # update apple new position
        self.rect.x = self.x
        self.rect.y = self.y

    def blit_apple(self):
        self.screen.blit(self.apple, (self.x, self.y))
