import pygame 
from pygame.locals import *
import random

# Initialise screen
pygame.init()
screen = pygame.display.set_mode((600, 480))
pygame.display.set_caption('zobizob')

# Fill background
background = pygame.Surface(screen.get_size())
background = background.convert()
background.fill((random.randint(0,150), random.randint(0,150), random.randint(0,150)))

# Blit everything to the screen
screen.blit(background, (0, 0))
pygame.display.flip()

# Event loop
continuer = 1
while continuer:
    for event in pygame.event.get():
        if event.type == QUIT:
            continuer = 0
    screen.blit(background, (0, 0))
    pygame.display.flip()
