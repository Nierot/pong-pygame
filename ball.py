import pygame
from random import randint
from const import *

class Ball(pygame.sprite.Sprite):

    def __init__(self, color, width, height):
        super().__init__()

        # set the color/width/heigth
        self.image = pygame.image.load('./miel.jpg')
        self.image = pygame.transform.scale(self.image, (100, 100))

        # draw the ball
        pygame.draw.rect(self.image, color, [0, 0, width, height])

        self.reset()

        self.rect = self.image.get_rect()

    def reset(self):
        self.speed = 1
        self.velocity = [randint(-4, 4), 1]

    def update(self):
        self.rect.x += self.velocity[0]
        self.rect.y += self.velocity[1]

    def bounce(self):
        self.speed += 0.03
        self.velocity[0] = -self.velocity[0] * self.speed
        self.velocity[1] = self.velocity[1] * self.speed