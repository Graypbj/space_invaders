import pygame
import random

# Initialize pygame
pygame.init()

# Create screen
screen = pygame.display.set_mode((800, 600))

# Background
background = pygame.image.load("assets/background.png")

# Title and Icon
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load('assets/image.png')
pygame.display.set_icon(icon)

# Player
playerImg = pygame.image.load('assets/player.png')
playerX = 800 // 2 - (playerImg.get_width() // 2)
playerY = 480
playerX_change = 0

# Enemy
enemyImg = pygame.image.load('assets/enemy.png')
enemyX = random.randint(0, 800)
enemyY = random.randint(50, 150)
enemyX_change = 0.3
enemyY_change = 40

def player(x, y):
    screen.blit(playerImg, (x, y))

def enemy(x, y):
    screen.blit(enemyImg, (x, y))

# Game Loop
running = True
while running:
    # RGB - Red, Green, Blue
    screen.fill((0, 0, 0))

    # Background image
    screen.blit(background, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # if keystroke is pressed, check whether it is right or left
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -0.5
            if event.key == pygame.K_RIGHT:
                playerX_change = 0.5
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0

    # Checking for boundaries of spaceship so it doesn't go out of bounds
    playerX += playerX_change
    
    if playerX < 0:
        playerX = 0
    elif playerX >=736:
        playerX = 736

    # Enemy movement
    enemyX += enemyX_change

    if enemyX < 0:
        enemyX_change = 0.3
        enemyY += enemyY_change
    elif enemyX >=736:
        enemyX_change = -0.3
        enemyY += enemyY_change

    # Draw the assets after screen has been drawn
    player(playerX, playerY)
    enemy(enemyX, enemyY)

    # Updates any changes made to the screen
    pygame.display.update()

