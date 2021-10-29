import pygame
import colors
import constantVariables

def gameOverScreen():
    gameOverFont = pygame.font.Font('freesansbold.ttf',64)

    gameOverText = gameOverFont.render("Game Over",True,colors.white)
    constantVariables.screen.blit(gameOverText,(200,250))