import pygame
import sqlite3
from sys import argv


conn = sqlite3.connect('database.db')
cursor = conn.cursor()
main_screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption('poi')
clock = pygame.time.Clock()
background = pygame.image.load('background_game1.png')
score_image = pygame.image.load('score1.png')
run = True
pygame.init()
colour1 = pygame.Color('orange')
colour2 = pygame.Color('green')
colour3 = pygame.Color('white')
click_state = 0
x = 400
y = 300
opy_speed = 8
x_speed, y_speed = 5, 4
score = 0
player = pygame.Rect(10, 300, 50, 50)
striker = pygame.Rect(400, 300, 30, 30)
oponent = pygame.Rect(600, 300, 50, 50)
scorebox = pygame.Rect(790, 21, 100, 50)
score_text = ''
time = 'time'
base_font = pygame.font.Font(None, 30)
touch = 0
username = argv[1]
c = 0


def Score():
    main_screen.blit(score_image, (0, 28))


def bounce():
    global x_speed, y_speed, score, touch, c
    striker.x += x_speed
    striker.y += y_speed
    if striker.right >= 800 or striker.left <= 0:
        x_speed *= -1
    if striker.bottom >= 600 or striker.top <= 0:
        y_speed *= -1
    if striker.colliderect(player):
        touch = 0

        if abs(striker.bottom - player.top) < 10:
            y_speed *= -1
        if abs(striker.top - player.bottom) < 10:
            y_speed *= -1
        if abs(striker.right - player.left) < 10:
            x_speed *= -1
        if abs(striker.left - player.right) < 10:
            x_speed *= -1
        if abs(striker.bottomleft[0]-player.topright[0]) < 10 or abs(striker.bottomleft[1]-player.topright[1]) < 10:
            x_speed *= -1
            y_speed *= -1
        if abs(player.bottomleft[0]-striker.topright[0]) < 10 or abs(player.bottomleft[1]-striker.topright[1]) < 10:
            x_speed *= -1
            y_speed *= -1
        if abs(striker.bottomright[0]-player.topleft[0]) < 10 or abs(striker.bottomright[1]-player.topleft[1]) < 10:
            x_speed *= -1
            y_speed *= -1
        if abs(player.bottomright[0]-striker.topleft[0]) < 10 or abs(player.bottomright[1]-striker.topleft[1]) < 10:
            x_speed *= -1
            y_speed *= -1
    if striker.colliderect(oponent):
        # print('hi')
        touch = 1
        c += 1
        if abs(striker.bottom - oponent.top) < 5:
            y_speed *= -1

            touch = 1
        if abs(striker.top - oponent.bottom) < 5:
            y_speed *= -1

            touch = 1
        if abs(striker.right - oponent.left) < 5:
            x_speed *= -1

            touch = 1
        if abs(striker.left - oponent.right) < 5:
            x_speed *= -1

            touch = 1
        if abs(striker.bottomleft[0]-oponent.topright[0]) < 10 or abs(striker.bottomleft[1]-oponent.topright[1]) < 10:
            x_speed *= -1
            y_speed *= -1
        if abs(oponent.bottomleft[0]-striker.topright[0]) < 10 or abs(oponent.bottomleft[1]-striker.topright[1]) < 10:
            x_speed *= -1
            y_speed *= -1
        if abs(striker.bottomright[0]-oponent.topleft[0]) < 10 or abs(striker.bottomright[1]-oponent.topleft[1]) < 10:
            x_speed *= -1
            y_speed *= -1
        if abs(oponent.bottomright[0]-striker.topleft[0]) < 10 or abs(oponent.bottomright[1]-striker.topleft[1]) < 10:
            x_speed *= -1
            y_speed *= -1
        if c > 1:
            striker.x = 400
            striker.y = 300
            c = 0
        else:
            c = 0
    pygame.draw.rect(main_screen, colour3, striker)


def Background():
    main_screen.blit(background, (0, 0))


def colinear(x1, x2, x3, y1, y2, y3):
    a = x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)
    if a == 0:
        return True
    else:
        return False


def find_col(x1, x2, x3, y1, y2):
    return ((x2*y1) - (x1*y2) - (x3*y1) + (x3*y2))/(x2 - x1)


while run:
    mouse = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            text = 'update playerinfo set poi = ? where user_name = ?'
            cursor.execute(text, (score, username))
            conn.commit()
            run = False
        if event.type == pygame.MOUSEBUTTONUP:
            click_state = 1
            print(mouse)

    main_screen.fill((0, 0, 0))
    Background()
    bounce()
    Score()

    if player.x > 400:
        click_state = 0
    if click_state == 1:
        player.x = mouse[0]
        player.y = mouse[1]
        pygame.draw.rect(main_screen, colour1, player)
    else:
        player.x = 10
        player.y = 300
        pygame.draw.rect(main_screen, colour1, player)

    x1 = striker.x
    y1 = striker.y
    if y_speed < 0:
        x2 = striker.x - 1
        y2 = striker.y - 1
    else:
        x2 = striker.x + 1
        y2 = striker.y + 1

    a = find_col(x1, x2, oponent.x, y1, y2) - 5

    if a < 550:
        oponent.y = a
    else:
        oponent.y = 300
    pygame.draw.rect(main_screen, colour2, oponent)
    if striker.x > 750 and striker.y > 200 and striker.y < 400:
        striker.x = 400
        striker.y = 300
        pygame.draw.rect(main_screen, colour3, oponent)
        score += 4
    if striker.x < 10 and striker.y > 200 and striker.y < 400:
        striker.x = 400
        striker.y = 300
        pygame.draw.rect(main_screen, colour3, oponent)
        score -= 1
    if score == 20:
        text = 'update playerinfo set poi = ? where user_name = ?'
        cursor.execute(text, (score, username))
        conn.commit()
        run = False

    score_text = str(score)
    score_surface = base_font.render(score_text, True, (255, 69, 0))
    main_screen.blit(score_surface, (90, 40))
    clock.tick(60)
    pygame.display.flip()
    pygame.display.update()
