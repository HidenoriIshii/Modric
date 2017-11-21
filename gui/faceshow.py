# -*- coding: utf-8 -*-
import pygame
import cv2

class FaceShow():
    def __init__(self,width,height):
        pygame.init()
        size = (width,height)
        self.screen = pygame.display.set_mode(size)

    def imshow(array):
        b,g,r = cv2.split(array)
        rgb = cv2.merge([r,g,b])
        surface1 = pygame.surfarray.make_surface(rgb)
        surface2 = pygame.transform.rotate(surface1, -90)
        surface3 = pygame.transform.flip(surface2, True, False)
        screen.blit(surface3, (0,0))
        pygame.display.flip()
                
