#
# To do
#
#

import pygame
import random
import math
import shelve

pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((800,600))

firstTime = True
gameOverScreen = False

pygame.display.set_caption("Flappy Bird pero mas pro")
icon = pygame.image.load('images/flappy.png')
pygame.display.set_icon(icon)

scoreValue = 0
maxScore = 0
font = pygame.font.Font('freesansbold.ttf', 32)
gameOverFont = pygame.font.Font('freesansbold.ttf', 64)
playAgain = pygame.font.Font('freesansbold.ttf', 50)
textX = 10
textY = 10

def load():
    try:
        f = shelve.open("save.bin")
        return f['maxScore']
    except KeyError:
        return 0
    finally:
        f.close()
 

def gameOver():
    gameOverText = gameOverFont.render("GAME OVER",True,(0,0,0))
    screen.blit(gameOverText,(200,250))

def showScore(x, y):
    scoreText = font.render("Score: "+ str(scoreValue), True,(0,0,0))
    screen.blit(scoreText,(x,y))

def showMaxScore(x, y):
    maxScoreText = font.render("Max Score: "+ str(maxScore), True,(0,0,0))
    screen.blit(maxScoreText,(x,y))

def showPlayAgain():
    playAgainText = font.render("Press enter to play again", True,(0,0,0))
    screen.blit(playAgainText,(200,340))

jump = 0
playerImg = pygame.image.load('Images/flappy.png')
playerX = 100
playerY = 300
def player(x,y):
    screen.blit(playerImg,(x,y))

def save(maxScore):
    f = shelve.open("save.bin")
    f['maxScore'] = maxScore
    f.close()


pipeImg = []
pipeTop = []
pipeDown = []
pipeX = []
pipeChangeX = 0.1
numOfPipes = 6

position = 250
firstPosition = 250
for i in range(numOfPipes):
    pipeX.append(position)
    position += 200
    # pipe ???
    pipeTop.append(random.randint(40,340))
    pipeDown.append(pipeTop[i]+180)

def resetPipes():
    actualPosition = firstPosition
    for i in range(numOfPipes):
        pipeX[i] = actualPosition
        actualPosition += 200
        pipeTop[i] = random.randint(40,340)
        pipeDown[i] = pipeTop[i] + 180
        pipeChangeX = 0.1


def isCollision(playerX,playerY,pipeX,pipeTop,pipeDown):
    if pipeX <= playerX and playerX <= pipeX + 50:
        if playerY<=pipeTop or pipeDown <= playerY:
            return True
        else:
            return False
    else:
        return False

position -= 250
running = True

maxScore = load() 
while running:
    screen.fill((0,255,255))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            maxScore = max(scoreValue,maxScore)
            save(maxScore)
            running = False
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                jump = 150
            if event.key == pygame.K_RETURN:
                gameOverScreen = False
                resetPipes()
                pipeChangeX = 0.1
                playerY = 300
    if jump > 0:
        playerY -= 0.8
        jump -= 1
    else:
        playerY += 0.3
    if playerY < 0:
        playerY = 0
    elif playerY + 32 > 600:
        gameOverScreen = True
    for i in range(numOfPipes):
        pipeX[i] -= pipeChangeX
        if pipeX[i] < 0:
            pipeX[i] = position
            pipeTop[i] =random.randint(40,340)
            pipeDown[i] = pipeTop[i]+180
            if gameOverScreen == False:
                scoreValue += 1
                if scoreValue%4 == 0 and scoreValue > 0:
                    pipeChangeX += 0.15
        collision = isCollision(playerX,playerY,pipeX[i],pipeTop[i],pipeDown[i])
        if collision and gameOverScreen == False:
            maxScore = max(maxScore,scoreValue)
            scoreValue = 0
            gameOverScreen = True
        if gameOverScreen == False:
            pygame.draw.rect(screen,(0,255,0),(pipeX[i],0,40,pipeTop[i])),
            pygame.draw.rect(screen,(0,255,0),(pipeX[i],pipeDown[i],40,600))
    if gameOverScreen == False:
        player(playerX,playerY)
    if gameOverScreen == True:
        gameOver()
    showScore(textX,textY)
    showMaxScore(textX,textY+40)
    if gameOverScreen == True:
        showPlayAgain()
    pygame.display.update()