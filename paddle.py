import pygame
from const import *

class Paddle(pygame.sprite.Sprite):

    def __init__(self, color, width, heigth):
        super().__init__()

        self.image = pygame.Surface([width, heigth])
        self.image.fill(BLACK)
        self.image.set_colorkey(BLACK)

        pygame.draw.rect(self.image, color, [0, 0, width, heigth])

        self.rect = self.image.get_rect()

    def move_up(self, px):
        self.rect.y -= px

        # do not go off screen
        if self.rect.y < 0:
            self.rect.y = 0

    def move_down(self, px):
        self.rect.y += px

        # do not go off screen
        if self.rect.y > SIZE[1] - self.image.get_height():
            self.rect.y = SIZE[1] - self.image.get_height()