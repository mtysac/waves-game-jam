import sys, os
import pygame

pygame.init()

ICON_PATH = "assets/images/player.png"
game_icon = pygame.image.load(os.path.join(ICON_PATH)) 
pygame.display.set_icon(game_icon)
SCREEN = pygame.display.set_mode((1280, 720), pygame.RESIZABLE)
