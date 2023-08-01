# Example file showing a basic pygame "game loop"
# import pygame

# pygame setup
# pygame.init()
# screen = pygame.display.set_mode((1280, 720))
# clock = pygame.time.Clock()
# running = True

# while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    # for event in pygame.event.get():
        # if event.type == pygame.QUIT:
            # running = False

    # fill the screen with a color to wipe away anything from last frame
#screen.fill("light blue")

    # RENDER YOUR GAME HERE

    # flip() the display to put your work on screen
    # pygame.display.flip()

    # clock.tick(60)  # limits FPS to 60

# pygame.quit()





#~~~~~~~~~~~~~

import pygame
import os 

from Player import Player
from Enemy import Enemy
from Map import Map

# 1.Init Game
pygame.init

# 2 Screen Setting
pygame.display.set_caption("Geometry Dash")

SIZE = (1280,720)
FPS = 60


windowScreen = pygame.display.set_mode(SIZE)
windowScreen.fill("light blue")
clock = pygame.time.Clock()

#background = pygame.image.load('retro.png')


# 3 Setting main function

def main():
    player_1 = Player(200, 200, 50, 50)
    enemy_1 = Enemy(10, 10, 50, 50)
    # gravity = 4
    
    isRunning = True
    while isRunning:
        
        # enemy_1.bottom += gravity
        # collide = pygame.Rect.colliderect(player_1, enemy_1)
        # if collide:
        #     enemy_1.bottom = player_1.top
        
        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
                isRunning = False
                
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            player_1.move(-10, 0)
        if keys[pygame.K_d]:
            player_1.move(10, 0)
        if keys[pygame.K_w]:
            player_1.move(0, -10)
        if keys[pygame.K_s]:
            player_1.move(0, 10)
            

        if keys[pygame.K_LEFT]:
            enemy_1.move(-10, 0)
        if keys[pygame.K_RIGHT]:
            enemy_1.move(10, 0)
        if keys[pygame.K_UP]:
            enemy_1.move(0, -10)
        if keys[pygame.K_DOWN]:
            enemy_1.move(0, 10)
        
        windowScreen.fill("purple")
    
        
        # player_1.handlePlayerMove()
        player_1.selfDrawingToTheScreen(windowScreen)
        enemy_1.selfDrawingToTheScreen(windowScreen)
        pygame.display.flip()
        clock.tick(FPS)
        
        
if __name__ == "__main__":
    main()
    

	
    



    
    

		

