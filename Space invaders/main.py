import pygame
import random
import math
from pygame import mixer

pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((800, 600))

# Title
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load('images/ufo.png')
pygame.display.set_icon(icon)

mixer.music.load('Sounds/background.wav')
mixer.music.play(-1)

background = pygame.image.load('images/background.png')

scoreValue = 0
font = pygame.font.Font('freesansbold.ttf', 32)
overFont = pygame.font.Font('freesansbold.ttf', 64)

textX = 10
textY = 10


def gameOver():
    overText = overFont.render("GAME OVER", True, (255, 255, 255))
    screen.blit(overText, (200, 250))


def showScore(x, y):
    score = font.render("Score :" + str(scoreValue), True, (255, 255, 255))
    screen.blit(score, (x, y))


# player Image

playerImg = pygame.image.load('images/player.png')

playerX = 370
playerY = 480
playerChangeY = 0
playerChangeX = 0


def player(x, y):
    screen.blit(playerImg, (x, y))


# enemies
enemyImg = []
enemyX = []
enemyY = []
enemyChangeX = []
enemyChangeY = []
numOfEnemies = 6
for i in range(numOfEnemies):
    enemyImg.append(pygame.image.load('images/enemy.png'))
    enemyX.append(random.randint(0, 800))
    enemyY.append(random.randint(50, 150))
    enemyChangeX.append(-2.5)
    enemyChangeY.append(30)


def enemy(x, y, i):
    screen.blit(enemyImg[i], (x, y))


# bullet
bulletImg = pygame.image.load('images/bullet.png')
bulletX = 0
bulletY = 480
bulletChangeX = 0
bulletChangeY = 5
bulletState = "ready"


def fire_bullet(x, y):
    global bulletState
    bulletState = "fire"
    screen.blit(bulletImg, (x + 16, y - 10))


# Detect Collision
def isCollision(enemyX, enemyY, bulletX, bulletY, bulletState):
    distance = math.sqrt(math.pow(enemyX - bulletX, 2) + math.pow(enemyY - bulletY, 2))
    if distance < 27 and bulletState is "fire":
        return True
    else:
        return False


# Game loop
running = True
while running:
    screen.fill((0, 0, 0))
    screen.blit(background, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerChangeX = -2
            if event.key == pygame.K_RIGHT:
                playerChangeX = 2
            if event.key == pygame.K_UP:
                playerChangeY = -2
            if event.key == pygame.K_DOWN:
                playerChangeY = 2
            if event.key == pygame.K_SPACE:
                if bulletState is "ready":
                    bulletSound = mixer.Sound('Sounds\laser.wav')
                    bulletSound.play()
                    bulletY = playerY
                    bulletX = playerX
                    fire_bullet(bulletX, bulletY)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerChangeX = 0
            if event.key == pygame.K_DOWN or event.key == pygame.K_UP:
                playerChangeY = 0

    if (playerX + playerChangeX + 50 < 800 and playerX + playerChangeX > 0):
        playerX += playerChangeX

    if (playerY + playerChangeY + 50 < 600 and playerY + playerChangeY > 0):
        playerY += playerChangeY

    for i in range(numOfEnemies):
        if (enemyX[i] + enemyChangeX[i] < 0):
            enemyChangeX[i] = 2.5
            enemyY[i] += enemyChangeY[i]
            if (enemyY[i] + 50 > 600):
                for j in range(numOfEnemies):
                    enemyY[j] = -200000
                gameOver()
        elif (enemyX[i] + enemyChangeX[i] + 50 > 800):
            enemyChangeX[i] = -2.5
            enemyY[i] += enemyChangeY[i]
            if (enemyY[i] + 50 > 600):
                for j in range(numOfEnemies):
                    enemyY[j] = -200000
                gameOver()

    if bulletState is "fire":
        fire_bullet(bulletX, bulletY)
        bulletY -= bulletChangeY
        if (bulletY < 0):
            bulletState = "ready"

    for i in range(numOfEnemies):
        enemyX[i] += enemyChangeX[i]

    for i in range(numOfEnemies):
        collision = isCollision(enemyX[i], enemyY[i], bulletX, bulletY, bulletState)
        if collision:
            explosionSound = mixer.Sound('Sounds\explosion.wav')
            explosionSound.play()
            bulletState = "ready"
            scoreValue += 1
            enemyX[i] = random.randint(0, 735)
            enemyY[i] = random.randint(50, 100)
        enemy(enemyX[i], enemyY[i], i)

    player(playerX, playerY)
    showScore(textX, textY)
    pygame.display.update()
