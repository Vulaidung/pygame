import pygame
import os



class Player(pygame.sprite.Sprite):
    PLAYER_COLOR = (250, 0, 0)
    def __init__(self, x, y, width, height):
        self.rect = pygame.Rect(x, y, width, height)
        
      
    def move(self, dx, dy):
        self.rect.x += dx
        self.rect.y += dy
        
    def selfDrawingToTheScreen(self, windowScreen):
        pygame.draw.rect(windowScreen, self.PLAYER_COLOR, self.rect)
    

#player_img = pygame.image.load('img/Tiled blocks.png')

playerImg = pygame.image.load('Tiled blocks.png')
playerX = 370
playerY = 480
