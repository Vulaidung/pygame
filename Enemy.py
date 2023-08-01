import pygame
import os



class Enemy(pygame.sprite.Sprite):
    ENEMY_COLOR = (0, 120, 0)
    def __init__(self, x, y, width, height):
        self.rect = pygame.Rect(x, y, width, height)
        
      
    def move(self, dx, dy):
        self.rect.x += dx
        self.rect.y += dy
        
    def selfDrawingToTheScreen(self, windowScreen):
        pygame.draw.rect(windowScreen, self.ENEMY_COLOR, self.rect)