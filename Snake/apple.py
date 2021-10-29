import pygame
import numpy as np
import random

from pygame.constants import SCALED
import colors
import constantVariables
import snake

class Apple:
    def __init__(self,Snake):
        self.row = random.randint(0,constantVariables.rows-1)
        self.column = random.randint(0,constantVariables.columns-1)
        self.snake = Snake
        t = True
        while (t):
            x = self.snake.snakeLength()
            print(x)
            print(self.snake.body)
            for i in range(x):

                if self.snake.body[i][0] == self.row and self.snake.body[i][1] == self.column:
                    self.row = random.randint(1,constantVariables.rows)
                    self.column = random.randint(1,constantVariables.columns)
                    i = 0
                t = False
        return
        
    def appleCoords(self):
        return (self.row,self.column)
