#Classic arcade game for two players.

import pygame, random, math, time

pygame.init()

#game colors
red = (255, 0, 0)
green = (0, 255, 0)
orange = (218, 176, 39)
white = (255, 255, 255)
black = (0, 0, 0)

def game_ui():
    screen_width = 600
    screen_lengh = 400
    screen_area = pygame.display.set_mode((screen_width, screen_lengh))
    pygame.display.set_caption('Enjoy Ping-pong!')
    pygame.font.SysFont("arial", 30, bold=True)

#define ball starting position
    ball_x_axis = int(screen_width / 2)
    ball_y_axis = int(screen_lengh / 2)

#define how far ball will move on (distance in pixels)
    ball_x_move = 3
    ball_y_move = 3
    ball_size = 25

    paddleA_xaxis_position = 10
    paddleA_yaxis_position = 10
    paddleA_width = 25
    paddleA_heigh = 100

    paddleB_xaxis_position = (screen_width - 35)
    paddleB_yaxis_position = 10
    paddleB_width = 25
    paddleB_heigh = 100

    first_player_score = 0
    second_player_score = 0

def main():
    program_run = True
    pygame.mouse.set_visible(False)
    while program_run is True:
        game_ui()
        


