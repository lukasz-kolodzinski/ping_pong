#Classic arcade game for two players.

import pygame, random, math, time

pygame.init()

#game colors
red = (255, 0, 0)
green = (0, 255, 0)
orange = (218, 176, 39)
white = (255, 255, 255)
black = (0, 0, 0)

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

program_run = True
pygame.mouse.set_visible(False)
while program_run is True:
    pressed_button = pygame.key.get_pressed()
    pygame.key.set_repeat()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            program_run = False
    if pressed_button [pygame.K_ESCAPE]:
        program_run = False
    if pressed_button [pygame.K_w]:
        paddleA_yaxis_position -= 5
    if pressed_button [pygame.K_s]:
        paddleA_yaxis_position += 5
    if pressed_button [pygame.K_UP]:
        paddleB_yaxis_position -= 5
    if pressed_button [pygame.K_DOWN]:
        paddleB_yaxis_position += 5

ball_x_axis += ball_x_move
ball_y_axis += ball_y_move
# Cushion colision detection
if ball_y_axis - ball_size <= 0 or ball_y_axis + ball_size >= screen_lengh:
    ball_y_move *= -1

if paddleA_yaxis_position < 0:
    paddleA_yaxis_position = 0
elif paddleA_yaxis_position + paddleA_heigh > screen_lengh:
    paddleA_yaxis_position = screen_lengh - paddleA_heigh

if paddleB_yaxis_position < 0:
    paddleB_yaxis_position = 0
elif paddleB_yaxis_position + paddleB_heigh > screen_lengh:
    paddleB_yaxis_position = screen_lengh - paddleB_heigh

#left paddle ball collision
if ball_x_axis < paddleA_xaxis_position + paddleA_width and ball_y_axis >= paddleA_yaxis_position and ball_y_axis <= paddleA_yaxis_position + paddleA_heigh:
    ball_x_move *= -1

#right paddle ball collison
if ball_x_axis > paddleB_xaxis_position and ball_y_axis >= paddleB_yaxis_position and ball_y_axis <= paddleB_yaxis_position + paddleB_heigh:
    ball_x_move *= -1

#determine when player2 scores
if ball_x_axis <= 0:
    second_player_score += 1
    ball_x_axis = int(screen_width /2)
    ball_y_axis = int(screen_lengh /2)
elif ball_y_axis >= screen_width:
    first_player_score +=1
    ball_x_axis = int(screen_width /2)
    ball_y_axis = int(screen_lengh /2)

#graphical content
screen_area.fill(green)
paddleA = pygame.draw.rect(screen_area,red,(paddleA_xaxis_position, paddleA_yaxis_position, paddleA_heigh, paddleA_width), 0)
paddleB = pygame.draw.rect(screen_area,red,(paddleB_xaxis_position,paddleB_yaxis_position,paddleB_heigh,paddleB_width),0)
net = pygame.draw.line(screen_area,black,(300,5),(300,400))
ball = pygame.draw.circle(screen_area,orange,(ball_x_axis,ball_y_axis),ball_size,0)

#score display
score = font.render(str(first_player_score) + " " + str(second_player_score), 1, white)
screen_area.blit(score, (screen_width /2 - score.get_width() /2, 10))






