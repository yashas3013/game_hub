import pygame
import random
from sys import argv
from math import radians, sin, cos
import sqlite3
conn = sqlite3.connect('database.db')
cursor = conn.cursor()



main_screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption('STAR WARS')
pygame.init()
background = pygame.image.load('background1.png')
ship = pygame.image.load('sp1.png')
missile = pygame.image.load('missile.png')
enemy1 = pygame.image.load('enemy1.png')
enemy2 = pygame.image.load('enemy1.png')
enemy3 = pygame.image.load('enemy1.png')
missiles = pygame.image.load('missiles.png')
score_image = pygame.image.load('score1.png')
player_x = 360
player_y = 480
player_xchange = 0
missile_x = player_x
missile_y = 480
missile_ychange = -2
state = 0
limit1_x = (100, 200)
limit1_y = (100, 200)
limit2_x = (450, 650)
limit2_y = (200, 300)
limit3_x = (300, 400)
limit3_y = (50, 150)
list_limit = [(limit1_x, limit1_y), (limit2_x, limit2_y), (limit3_x, limit3_y)]
random.shuffle(list_limit)
enemy1_x = random.randint(list_limit[0][0][0], list_limit[0][0][1])
enemy1_y = random.randint(list_limit[0][1][0], list_limit[0][1][1])
enemy2_x = random.randint(list_limit[1][0][0], list_limit[1][0][1])
enemy2_y = random.randint(list_limit[1][1][0], list_limit[1][1][1])
enemy3_x = random.randint(list_limit[2][0][0], list_limit[2][0][1])
enemy3_y = random.randint(list_limit[2][1][0], list_limit[2][1][1])
angle1 = 0
angle2 = 0
angle3 = 0
kill_enemy1 = 0
kill_enemy2 = 0
kill_enemy3 = 0
score = 0
score_text = ''
base_font = pygame.font.Font(None, 30)
base_font1 = pygame.font.Font(None, 32)
missiles_left = '5'
final = 0
missile_shadow = pygame.Rect(missile_x, missile_y, 3.2, 3.2)
enemy1_shadow = pygame.Rect(enemy1_x, enemy1_y, 3.2, 3.2)
enemy2_shadow = pygame.Rect(enemy2_x, enemy2_y, 3.2, 3.2)
enemy3_shadow = pygame.Rect(enemy3_x, enemy3_y, 3.2, 3.2)
colour3 = pygame.Color('white')
x_speed = 1
y_speed = 1
username = argv[1]



def Score():
    main_screen.blit(score_image, (0, 28))


def Missiles():
    main_screen.blit(missiles, (680, 40))


def Enemy3(enemy_x, enemy3_y):
    main_screen.blit(enemy3, (enemy3_x, enemy3_y))


def Enemy1(enemy1_x, enemy_y):
    main_screen.blit(enemy1, (enemy1_x, enemy1_y))


def Enemy2(enemy2_x, enemy2_y):
    main_screen.blit(enemy2, (enemy2_x, enemy2_y))


def Background():
    main_screen.blit(background, (0, 0))


def Player(player_x, player_y):
    main_screen.blit(ship, (player_x, player_y))


def Misile(missile_x, missile_y):
    global state
    state = 1
    main_screen.blit(missile, (missile_x + 16, missile_y + 10))


def cords(angle, radius, coords):
    theta = radians(angle)
    return coords[0] + radius * cos(theta), coords[1] + radius * sin(theta)


run = True
while run:
    mouse = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            text = 'update playerinfo set spacewars = ? where user_name = ?'
            cursor.execute(text, (score, username))
            # cursor.execute(text, (score,))
            conn.commit()
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player_xchange = -2
            if event.key == pygame.K_RIGHT:
                player_xchange = +2
            if event.key == pygame.K_SPACE:
                if state == 0:
                    missile_x = player_x
                    Misile(missile_x, 480)
                    missiles_left = int(missiles_left) - 1
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                player_xchange = 0
    Background()
    player_x += player_xchange
    if kill_enemy1 == 0:
        angle1 += 2
        cord1 = cords(angle1, 75, (enemy1_x, enemy1_y))
        a1 = cord1[0]
        b1 = cord1[1]

    else:
        a1 = -100
        b1 = -90
    if kill_enemy2 == 0:
        angle2 += 2
        cord2 = cords(angle2, 75, (enemy2_x, enemy2_y))
        a2 = cord2[0]
        b2 = cord2[1]

    else:
        a2 = -100
        b2 = -90
    if kill_enemy3 == 0:
        angle3 += 2
        cord3 = cords(angle3, 75, (enemy3_x, enemy3_y))
        a3 = cord3[0]
        b3 = cord3[1]
    else:
        a3 = 1000
        b3 = 900

    Enemy3(a3, b3)
    Enemy2(a2, b2)
    Enemy1(a1, b1)
    enemy1_shadow = pygame.Rect(a1 + 15, enemy1_y + 10, 40, 40)
    enemy2_shadow = pygame.Rect(a2 + 15, b2 + 10, 40, 40)
    enemy3_shadow = pygame.Rect(enemy3_x+15, b3 + 10, 40, 40)
    if missile_y < 0:
        state = 0
        final = 1
        missile_y = 480
    if state == 1:
        Misile(missile_x, missile_y)
        missile_y += missile_ychange
    if player_x < 0:
        player_xchange = 0
    if player_x > 737:
        player_xchange = 0

    Player(player_x, player_y)

    if state == 1:
        shoot_radius = 10
        if missile_shadow.colliderect(enemy1_shadow):
            if abs(missile_shadow.top - enemy1_shadow.bottom) < shoot_radius:
                missile_y = 480
                state = 0
                kill_enemy1 = 1
                score += 2
            elif abs(missile_shadow.right - enemy1_shadow.left) < shoot_radius:
                missile_y = 480
                state = 0
                kill_enemy1 = 1
                score += 2
            elif abs(missile_shadow.left - enemy1_shadow.right) < shoot_radius:
                missile_y = 480
                state = 0
                kill_enemy1 = 1
                score += 2
        if missile_shadow.colliderect(enemy2_shadow):
            if abs(missile_shadow.top - enemy2_shadow.bottom) < shoot_radius:
                missile_y = 480
                state = 0
                kill_enemy2 = 1
                score += 3
            elif abs(missile_shadow.right - enemy2_shadow.left) < shoot_radius:
                missile_y = 480
                state = 0
                kill_enemy2 = 1
                score += 3
            elif abs(missile_shadow.left - enemy2_shadow.right) < shoot_radius:
                missile_y = 48
                state = 0
                kill_enemy2 = 1
                score += 3
        if missile_shadow.colliderect(enemy3_shadow):
            if abs(missile_shadow.top - enemy3_shadow.bottom) < shoot_radius:
                missile_y = 480
                state = 0
                kill_enemy3 = 1
                score += 1
            elif abs(missile_shadow.bottom - enemy3_shadow.top) < shoot_radius:
                missile_y = 480
                state = 0
                kill_enemy3 = 1
                score += 1
            elif abs(missile_shadow.right - enemy3_shadow.left) < shoot_radius:
                missile_y = 480
                state = 0
                kill_enemy3 = 1
                score += 1
            elif abs(missile_shadow.left - enemy3_shadow.right) < shoot_radius:
                missile_y = 480
                state = 0
                kill_enemy3 = 1
                score += 1

        if int(missiles_left) < 0 or score >= 6 and final == 1:
            cursor.execute('update score set spacewars = 0;')
            text = 'update  score set spacewars = %s'
            text = 'update playerinfo set spacewars = ? where user_name = ?'
            cursor.execute(text, (score, username))
            conn.commit()
            run = False


    score_text = str(score)
    Missiles()
    Score()
    missiles_left = str(missiles_left)
    score_surface = base_font.render(score_text, True, (255, 69, 0))
    missiles_surface = base_font1.render(missiles_left, True, (255, 69, 0))
    main_screen.blit(score_surface, (90, 40))
    main_screen.blit(missiles_surface, (765, 80))
    missile_shadow = pygame.Rect(missile_x + 16, missile_y + 10, 32, 32)
    pygame.display.flip()
    pygame.display.update()
