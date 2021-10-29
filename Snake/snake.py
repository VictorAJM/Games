import pygame
import random
import math
import constantVariables
import colors
import numpy as np
import apple

class Snake:
    def __init__(self,screenSize):
        self.size = 3
        self.body = np.array([[3,3,1],[3,4,1],[3,5,-1]])
        self.moves = np.array([[-1,0],[0,1],[1,0],[0,-1]])

    def moveSnake(self,movement,appleObj):
        self.body[self.size-1][2] = movement
        head = np.copy(self.body[self.size-1])
        head[0] += self.moves[movement][0]
        head[1] += self.moves[movement][1]
        head[2] = movement
        if self.collision(head) == 1:
            return 0
        if head[0] == appleObj.appleCoords()[0] and head[1] == appleObj.appleCoords()[1]:
            self.increaseLength(movement)
            return 1
        else:
            for i in range(self.size-1):
                self.body[i] = self.body[i+1]

            self.body[self.size-1] = head
            return 2
        
    def increaseLength(self,movement):
        self.body[self.size-1][2] = movement
        head = np.copy(self.body[self.size-1])
        head[0] += self.moves[movement][0]
        head[1] += self.moves[movement][1]
        head[2] = movement

        self.body = np.append(self.body,[head],axis = 0)
        print(self.body)
        self.size += 1

    def snakeLength(self):
        return self.size

    def bodyCoord(self,position):
        return self.body[position]

    def collision(self,position):
        if position[0] < 0:
            return True
        if position[0] >= constantVariables.rows:
            return True
        if position[1] < 0:
            return True
        if position[1] >= constantVariables.columns:
            return True
        
        newBody = np.copy(self.body)
        for i in range(self.size-1):
            if newBody[i][0]+self.moves[newBody[i][2]][0] == position[0] and newBody[i][1]+self.moves[newBody[i][2]][1] == position[1]:
                return True

        return False
