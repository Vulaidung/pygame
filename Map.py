import pygame


#Pygame setup
pygame.init()
screen_width = 1200
screen_height = 850

screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()

retro_img = pygame.image.load('img/retro.png')

def draw_bg():
    screen.blit(retro_img, (0, 0))

running = True
while running:
    draw_bg() 
 
screen.blit(retro_img, (0, 0))



for event in pygame.event.get():
        if event.type == pygame.QUIT:
        
         running = False
         
pygame.display.update()

pygame.quit()