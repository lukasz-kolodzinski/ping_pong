#Classic arcade game for two players.

import pygame, random, math, time

pygame.init()

#game colors
red = (255, 0, 0)
green = (0, 255, 0)
orange = (218, 176, 39)
white = (255, 255, 255)
black = (0, 0. 0)

def game_screen():
    screen_width = 600
    screen_lengh = 400
    screen_area = pygame.display.set_mode((screen_width, screen_lengh))
    pygame.display.set_caption('Enjoy Ping-pong!')
    pygame.font.SysFont("arial", 30, bold=True)
    

