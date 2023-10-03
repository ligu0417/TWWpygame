"""
======================================================================
MAIN --- 

Main entry of the whole game tww.

    Author: Zi Liang <liangzid@stu.xjtu.edu.cn>
    Copyright © 2023, ZiLiang, all rights reserved.
    Created:  3 十月 2023
======================================================================
"""


import pygame





pygame.init()
screen=pygame.display.set_mode((1280,720))
clock=pygame.time.Clock()
running=True
delta=0.


# ui surface
from tww_ui import progressBar




hp=progressBar()
mp=progressBar(x=330,color_tuple=(0,0,255),value=768,text=f"MP:")
while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("black")

    hp.build(screen)
    mp.build(screen)
    hp.current_alpha-=0.043
    mp.current_alpha-=0.02
    mp.current_alpha-=0.02
    mp.current_alpha-=0.02

    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000



    pass

    # keys = pygame.key.get_pressed()
    # if keys[pygame.K_w]:
    #     player_pos.y -= 300 * dt
    # if keys[pygame.K_s]:
    #     player_pos.y += 300 * dt
    # if keys[pygame.K_a]:
    #     player_pos.x -= 300 * dt
    # if keys[pygame.K_d]:
    #     player_pos.x += 300 * dt

