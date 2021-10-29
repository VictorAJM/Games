from typing import Text
import pygame
import math
import shelve
import random
import colors
import firstTime
import gameOver
import constantVariables
import snake
import apple
import grid

pygame.init()

for i in range(3):
    print(i)

firstTimeFlag = True
gameOverFlag = False

pygame.display.set_caption("Snake")
icon = pygame.image.load('Images/snake.png')
pygame.display.set_icon(icon)

score = 0
maxScore = 0
font  = pygame.font.Font('freesansbold.ttf',32)
playAgain = pygame.font.Font('freesansbold.ttf',50)
textX = 10
textY = 10
Snake = snake.Snake(constantVariables.screenSize)
Apple = apple.Apple(Snake)
Grid = grid.Grid(constantVariables.screenSize[0],constantVariables.screenSize[1],Snake,Apple)
Grid.makeArray()
running = True
movement = -1
lastPressed = -1
while running:
    constantVariables.clock.tick(constantVariables.fps)
    constantVariables.screen.fill(colors.black)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            exit()
        if gameOverFlag == True:
            lastPressed = movement = -1
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    Snake = snake.Snake(constantVariables.screenSize)
                    Apple = apple.Apple(Snake)
                    Grid = grid.Grid(constantVariables.screenSize[0],constantVariables.screenSize[1],Snake,Apple)
                    Grid.makeArray()
                    firstTimeFlag = True
                    gameOverFlag = False
        elif firstTimeFlag == True:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        firstTimeFlag = False
                        movement = 0
                        lastPressed = 0
                    elif event.key == pygame.K_DOWN:
                        firstTimeFlag = False
                        movement = 2
                        lastPressed = 2
                    elif event.key == pygame.K_RIGHT:
                        firstTimeFlag = False
                        movement = 1
                        lastPressed = 1
                    else:
                        pass
        else:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and lastPressed != 2:
                    movement = 0
                    lastPressed = 0
                elif event.key == pygame.K_DOWN and lastPressed != 0:
                    movement = 2
                    lastPressed = 2
                elif event.key == pygame.K_RIGHT and lastPressed != 3:
                    movement = 1
                    lastPressed = 1
                elif event.key == pygame.K_LEFT and lastPressed != 1:
                    movement = 3
                    lastPressed = 3
                else:
                    pass
    if lastPressed != -1:
        respond = Snake.moveSnake(lastPressed,Apple)
        if respond != 0:
            if respond == 1:
                Apple = apple.Apple(Snake)
            Grid = grid.Grid(constantVariables.screenSize[0],constantVariables.screenSize[1],Snake,Apple)
            Grid.makeArray() 
        else: 
            gameOverFlag = True
    if gameOverFlag == False:
        Grid.drawGrid()
    else:
        gameOver.gameOverScreen()
    pygame.display.update()