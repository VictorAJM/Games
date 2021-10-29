import pygame
import numpy as np
import random
import constantVariables
import colors
import apple
import snake

class Grid:
    def __init__(self,width,height,snake,apple):
        self.scale = constantVariables.scale
        self.columns = constantVariables.columns
        self.rows = constantVariables.rows
        self.size = (self.rows,self.columns)
        self.gridArray = np.ndarray(shape = (self.size))
        self.offset = constantVariables.offset
        self.snake = snake
        self.apple = apple
    
    def makeArray(self):
        for i in range(self.rows):
            for j in range(self.columns):
                self.gridArray[i][j] = 0
        for i in range(self.snake.snakeLength()):
            self.gridArray[self.snake.bodyCoord(i-1)[0]][self.snake.bodyCoord(i-1)[1]] = 1
        self.gridArray[self.apple.appleCoords()[0]][self.apple.appleCoords()[1]] = 2

    def drawGrid(self):
        for i in range(self.rows):
            for j in range(self.columns):
                yPos = i * self.scale
                xPos = j * self.scale
                if self.gridArray[i][j] == 0:
                    pygame.draw.rect(constantVariables.screen,colors.white,[xPos,yPos,self.scale - self.offset,self.scale - self.offset])
                elif self.gridArray[i][j] == 1:
                    pygame.draw.rect(constantVariables.screen,colors.blue,[xPos,yPos,self.scale - self.offset,self.scale - self.offset])
                else: 
                     pygame.draw.rect(constantVariables.screen,colors.blue1,[xPos,yPos,self.scale - self.offset,self.scale - self.offset])