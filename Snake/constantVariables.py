import pygame
import random

from pygame.constants import SCALED

clock = pygame.time.Clock()
screenSize = (900,600)
scale = 30
screen = pygame.display.set_mode(screenSize)
rows = screenSize[1]//scale
columns = screenSize[0]//scale
offset = 1
fps = 5