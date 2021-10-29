import pygame
import numpy as np
import random

class Grid:
    def __init__(self, width, height, scale, offset):
        self.scale = scale
        self.columns = int(height/scale)
        self.rows = int(width/scale)
        self.size = (self.rows,self.columns)
        self.gridArray = np.ndarray(shape = (self.size))
        self.offset = offset
    
    def random2dArray(self):
        for x in range(self.rows):
            for y in range(self.columns):
                self.gridArray[x][y] = random.randint(0,1)
    
    def conway(self, offColor, onColor, surface, pause):
        for x in range(self.rows):
            for y in range(self.columns):
                yPos = y * self.scale
                xPos = x * self.scale
                if self.gridArray[x][y] == 1:
                    pygame.draw.rect(surface, onColor, [xPos, yPos, self.scale - self.offset, self.scale - self.offset])
                else:
                    pygame.draw.rect(surface, offColor, [xPos, yPos, self.scale - self.offset, self.scale - self.offset])
        
        next = np.ndarray(shape = (self.size))
        if pause == False:
            for x in range(self.rows):
                for y in range(self.columns):
                    state = self.gridArray[x][y]
                    neighbours = self.getNeighbours(x, y)
                    if state == 0 and neighbours == 3:
                        next[x][y] = 1
                    elif state == 1 and (neighbours < 2 or neighbours > 3):
                        next[x][y] = 0
                    else:
                        next[x][y] = state
            self.gridArray = next

    def handleMouse(self, x, y):
        _x = x//self.scale
        _y = y//self.scale

        next = np.ndarray(shape = (self.size))
        for i in range(self.rows):
            for j in range(self.columns):
                state = self.gridArray[i][j]
                next[i][j] = state
                if i == _x and j == _y:
                    next[i][j] = not next[i][j]
        self.gridArray = next

    def getNeighbours(self, x, y):
        total = 0
        for n in range(-1,2):
            for m in range(-1,2):
                xEdge = (x+n+self.rows) % self.rows
                yEdge = (y+m+self.columns) % self.columns
                total += self.gridArray[xEdge][yEdge]
        total -= self.gridArray[x][y]
        return total
    