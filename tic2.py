import pygame
import random
# import mysql.connector
import sqlite3
from sys import argv

conn = sqlite3.connect('database.db')
cursor = conn.cursor()
clock = pygame.time.Clock()
main_scren = pygame.display.set_mode((500, 500))
pygame.display.set_caption('tic tac toe')
pygame.init()
run = True
colour = pygame.Color('white')
colour1 = pygame.Color('red')

box1 = pygame.draw.rect(main_scren, colour, (50, 100, 100, 100))

box2 = pygame.draw.rect(main_scren, colour, (50, 220, 100, 100))

box3 = pygame.draw.rect(main_scren, colour, (50, 340, 100, 100))
box4 = pygame.draw.rect(main_scren, colour, (200, 100, 100, 100))

box5 = pygame.draw.rect(main_scren, colour, (350, 100, 100, 100))

box6 = pygame.draw.rect(main_scren, colour, (200, 220, 100, 100))

box7 = pygame.draw.rect(main_scren, colour, (350, 220, 100, 100))

box8 = pygame.draw.rect(main_scren, colour, (200, 340, 100, 100))

box9 = pygame.draw.rect(main_scren, colour, (350, 340, 100, 100))
object_state = 0
map_t = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0}
click_state = 0
WINDOW_WIDTH = 500
WINDOW_HEIGHT = 500
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
font = pygame.font.Font(None, 30)
username = argv[1]
text = ''


def win_screen1():
    global click_state
    global run
    base_font = pygame.font.Font(None, 60)
    text = 'YOU WIN'
    surface = base_font.render(text, True, (255, 0, 0))
    main_scren.blit(surface, (210, 45))
    click_state = 1
    score = 1
    text = 'update playerinfo set spacewars = ? where user_name = ?'
    # cursor.execute(text, (score, username))
    conn.commit()
    # run = False


def win_screen2():
    global run
    global click_state
    base_font = pygame.font.Font(None, 60)
    text = 'AI WINS,LOL'
    surface = base_font.render(text, True, (0, 0, 255))
    main_scren.blit(surface, (210, 45))
    click_state = 1
    score = 0
    # print(score)


def win_screen3():
    global run
    global click_state
    base_font = pygame.font.Font(None, 60)
    text = 'TIE'
    surface = base_font.render(text, True, (0, 0, 255))
    main_scren.blit(surface, (210, 45))
    click_state = 1


def win(map_t):
    if map_t[1] == 1 and map_t[2] == 1 and map_t[3] == 1:
        win_screen1()
    elif map_t[1] == 2 and map_t[2] == 2 and map_t[3] == 2:
        win_screen2()
    elif map_t[1] == 1 and map_t[4] == 1 and map_t[7] == 1:
        win_screen1()
    elif map_t[1] == 2 and map_t[4] == 2 and map_t[7] == 2:
        win_screen2()
    elif map_t[1] == 1 and map_t[5] == 1 and map_t[9] == 1:
        win_screen1()
    elif map_t[1] == 2 and map_t[5] == 2 and map_t[9] == 2:
        win_screen2()
    elif map_t[3] == 1 and map_t[5] == 1 and map_t[7] == 1:
        win_screen1()
    elif map_t[3] == 2 and map_t[5] == 2 and map_t[7] == 2:
        win_screen2()
    elif map_t[4] == 1 and map_t[5] == 1 and map_t[6] == 1:
        win_screen1()
    elif map_t[4] == 2 and map_t[5] == 2 and map_t[6] == 2:
        win_screen2()
    elif map_t[7] == 1 and map_t[8] == 1 and map_t[9] == 1:
        win_screen1()
    elif map_t[7] == 2 and map_t[8] == 2 and map_t[9] == 2:
        win_screen2()
    elif map_t[2] == 1 and map_t[5] == 1 and map_t[8] == 1:
        win_screen1()
    elif map_t[2] == 2 and map_t[5] == 2 and map_t[8] == 2:
        win_screen2()
    elif map_t[3] == 1 and map_t[6] == 1 and map_t[9] == 1:
        win_screen1()
    elif map_t[3] == 2 and map_t[6] == 2 and map_t[9] == 2:
        win_screen2()


click_count = 0
run = True
done = ['box1', 'box2', 'box3', 'box4', 'box5', 'box6', 'box7', 'box8', 'box9']
string = 'hi'
while run:

    if map_t[1] == 2 and map_t[2] == 2 and map_t[3] == 2:
        win_screen2()
    if map_t[9] == 2 and map_t[7] == 2 and map_t[8] == 2:
        win_screen2()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONUP and click_state == 0:
            click_count += 1
            win(map_t)
            mouse = pygame.mouse.get_pos()
            if map_t[1] == 2 and map_t[2] == 2 and map_t[3] == 2:
                win_screen2()
            if map_t[9] == 2 and map_t[7] == 2 and map_t[8] == 2:
                win_screen2()
            if box1.collidepoint(mouse) and 'box1' in done:
                pygame.draw.rect(main_scren, colour1, (60, 112, 80, 80))
                done.remove('box1')
                map_t[1] = 1
                object_state = 1
            if box2.collidepoint(mouse) and 'box2' in done:
                pygame.draw.rect(main_scren, colour1, (60, 232, 80, 80))
                object_state = 1
                done.remove('box2')
                map_t[4] = 1
            if box3.collidepoint(mouse) and 'box3' in done:
                pygame.draw.rect(main_scren, colour1, (60, 352, 80, 80))
                object_state = 1
                done.remove('box3')
                map_t[7] = 1
            if box4.collidepoint(mouse) and 'box4' in done:
                pygame.draw.rect(main_scren, colour1, (212, 112, 80, 80))
                object_state = 1
                done.remove('box4')
                map_t[2] = 1

            if box5.collidepoint(mouse) and 'box5' in done:
                pygame.draw.rect(main_scren, colour1, (360, 112, 80, 80))
                object_state = 1
                done.remove('box5')
                map_t[3] = 1
            if box6.collidepoint(mouse) and 'box6' in done:
                pygame.draw.rect(main_scren, colour1, (212, 232, 80, 80))
                object_state = 1
                done.remove('box6')
                map_t[5] = 1
            if box7.collidepoint(mouse) and 'box7' in done:
                pygame.draw.rect(main_scren, colour1, (360, 232, 80, 80))
                object_state = 1
                done.remove('box7')
                map_t[6] = 1
            if box8.collidepoint(mouse) and 'box8' in done:
                pygame.draw.rect(main_scren, colour1, (212, 352, 80, 80))
                object_state = 1
                done.remove('box8')
                map_t[8] = 1
            if box9.collidepoint(mouse) and 'box9' in done:
                pygame.draw.rect(main_scren, colour1, (360, 352, 80, 80))
                object_state = 1
                done.remove('box9')
                map_t[9] = 1

            if len(done) == 0:
                run = False
            elif len(done) == 8:
                box = random.choice(done)
                if map_t[1] == 1 or map_t[6] == 1 or map_t[4] == 1 or map_t[2] == 1 or map_t[8] == 1:
                    pygame.draw.circle(main_scren, (0, 0, 255), (250, 268), 30)
                    done.remove('box6')
                    map_t[5] = 2

                elif map_t[3] == 1:
                    pygame.draw.circle(main_scren, (0, 0, 255), (250, 268), 30)
                    done.remove('box6')
                    map_t[5] = 2
                elif map_t[7] == 1:
                    pygame.draw.circle(main_scren, (0, 0, 255), (250, 268), 30)
                    done.remove('box6')
                    map_t[5] = 2
                elif map_t[9] == 1:
                    pygame.draw.circle(main_scren, (0, 0, 255), (250, 268), 30)
                    done.remove('box6')
                    map_t[5] = 2
                elif map_t[5] == 1:
                    pygame.draw.circle(main_scren, (0, 0, 255), (100, 389), 30)
                    done.remove('box3')
                    map_t[7] = 2
                    win(map_t)
                elif map_t[2] == 1:
                    pygame.draw.circle(main_scren, (0, 0, 255), (400, 154), 30)
                    done.remove('box5')
                    map_t[3] = 2
                    win(map_t)
                elif map_t[6] == 1:
                    pygame.draw.circle(main_scren, (0, 0, 255), (400, 154), 30)
                    done.remove('box5')
                    map_t[3] = 2
                    win(map_t)
                elif map_t[4] == 1:
                    pygame.draw.circle(main_scren, (0, 0, 255), (100, 389), 30)
                    done.remove('box3')
                    map_t[7] = 2
                    win(map_t)
                elif map_t[8] == 1:
                    pygame.draw.circle(main_scren, (0, 0, 255), (100, 389), 30)
                    done.remove('box3')
                    map_t[7] = 2
                    win(map_t)
                else:
                    if box == 'box1':
                        pygame.draw.circle(main_scren, (0, 0, 255), (100, 154), 30)
                        done.remove('box1')
                        map_t[1] = 2
                        win(map_t)
                    if box == 'box2':
                        pygame.draw.circle(main_scren, (0, 0, 255), (100, 268), 30)
                        done.remove('box2')
                        map_t[4] = 2
                        win(map_t)
                    if box == 'box3':
                        pygame.draw.circle(main_scren, (0, 0, 255), (100, 389), 30)
                        done.remove('box3')
                        map_t[7] = 2
                        win(map_t)
                    if box == 'box5':
                        pygame.draw.circle(main_scren, (0, 0, 255), (400, 154), 30)
                        done.remove('box5')
                        map_t[3] = 2
                        win(map_t)
                    if box == 'box7':
                        pygame.draw.circle(main_scren, (0, 0, 255), (400, 268), 30)
                        done.remove('box7')
                        map_t[6] = 2
                        win(map_t)
                    if box == 'box8':
                        pygame.draw.circle(main_scren, (0, 0, 255), (250, 389), 30)
                        done.remove('box8')
                        map_t[8] = 2
                        win(map_t)
                    if box == 'box9':
                        pygame.draw.circle(main_scren, (0, 0, 255), (400, 389), 30)
                        done.remove('box9')
                        map_t[9] = 2
            # print(done)
            # print(map_t)
            if len(done) <= 6:
                win(map_t)
                # if map_t[3] == 1 and map_t[]
                if map_t[2] == 1 and map_t[4] == 1 and map_t[1] == 0 and 'box1' in done:
                    pygame.draw.circle(main_scren, (0, 0, 255), (100, 154), 30)
                    done.remove('box1')
                    map_t[1] = 2
                    win(map_t)
                elif map_t[3] == 1 and map_t[4] == 1 and map_t[5] == 0 and 'box1' in done:
                    # print(1)
                    pygame.draw.circle(main_scren, (0, 0, 255), (100, 154), 30)
                    done.remove('box1')
                    map_t[1] = 2
                    win(map_t)
                # elif map_t[2] == 1 and map_t[6] == 1 and
                elif map_t[9] == 1 and map_t[4] == 1 and 'box1' in done:

                    pygame.draw.circle(main_scren, (0, 0, 255), (100, 154), 30)
                    done.remove('box1')
                    map_t[1] = 2
                    win(map_t)
                elif map_t[1] == 1 and map_t[6] == 1 and 'box4' in done:
                    pygame.draw.circle(main_scren, (0, 0, 255), (250, 154), 30)
                    done.remove('box4')
                    map_t[2] = 2
                    win(map_t)
                elif map_t[3] == 1 and map_t[8] == 1 and 'box9' in done:

                    pygame.draw.circle(main_scren, (0, 0, 255), (400, 389), 30)
                    done.remove('box9')
                    map_t[9] = 2
                    win(map_t)
                elif map_t[1] == 1 and map_t[8] == 1 and 'box9' in done:

                    pygame.draw.circle(main_scren, (0, 0, 255), (400, 389), 30)
                    done.remove('box9')
                    map_t[9] = 2
                    win(map_t)
                elif map_t[4] == 1 and map_t[8] == 1 and 'box6' not in done and 'box3' in done:

                    pygame.draw.circle(main_scren, (0, 0, 255), (100, 389), 30)
                    done.remove('box3')
                    map_t[7] = 2
                    win(map_t)
                elif map_t[6] == 1 and map_t[8] == 1 and 'box6' not in done and 'box3' in done:

                    pygame.draw.circle(main_scren, (0, 0, 255), (100, 389), 30)
                    done.remove('box3')
                    map_t[7] = 2
                    win(map_t)
                elif map_t[2] == 1 and map_t[6] == 1 and map_t[5] != 1 and 'box5' in done:
                    pygame.draw.circle(main_scren, (0, 0, 255), (400, 154), 30)
                    done.remove('box5')
                    map_t[3] = 2
                    win(map_t)
                elif map_t[5] == 1 and map_t[3] == 1 and map_t[7] == 2 and 'box9' in done:
                    pygame.draw.circle(main_scren, (0, 0, 255), (400, 389), 30)
                    done.remove('box9')
                    map_t[9] = 2
                    win(map_t)
                elif map_t[2] == 1 and map_t[9] == 1 and map_t[8] != 1 and map_t[
                    5] != 1 and 'box6' not in done and 'box5' in done and 'box7' in done:
                    pygame.draw.circle(main_scren, (0, 0, 255), (400, 154), 30)
                    done.remove('box5')
                    map_t[3] = 2
                    win(map_t)
                elif map_t[2] == 1 and map_t[7] == 1 and map_t[8] != 1 and map_t[
                    5] != 1 and 'box6' not in done and 'box5' in done and 'box9' in done:
                    pygame.draw.circle(main_scren, (0, 0, 255), (400, 154), 30)
                    done.remove('box5')
                    map_t[3] = 2
                    win(map_t)
                elif map_t[2] == 1 and map_t[7] == 1 and map_t[5] == 0 and 'box6' in done:
                    pygame.draw.circle(main_scren, (0, 0, 255), (250, 268), 30)
                    done.remove('box6')
                    map_t[5] = 2
                    win(map_t)
                elif map_t[2] == 1 and map_t[9] == 1 and map_t[5] != 0 and 'box6' in done:

                    pygame.draw.circle(main_scren, (0, 0, 255), (250, 268), 30)
                    done.remove('box6')
                    map_t[5] = 2
                    win(map_t)

                elif map_t[8] == 1 and map_t[3] == 1 and 'box6' in done:
                    pygame.draw.circle(main_scren, (0, 0, 255), (250, 268), 30)
                    done.remove('box6')
                    map_t[5] = 2
                    win(map_t)
                elif map_t[8] == 1 and map_t[1] == 1 and 'box6' in done and box5 in done:
                    pygame.draw.circle(main_scren, (0, 0, 255), (250, 268), 30)
                    done.remove('box6')
                    map_t[3] = 2
                    win(map_t)
                elif map_t[5] == 1 and map_t[9] == 1 and 'box1' in done:
                    pygame.draw.circle(main_scren, (0, 0, 255), (100, 154), 30)
                    done.remove('box1')
                    map_t[1] = 2
                    win(map_t)

                elif map_t[3] == 1 and map_t[7] == 1 and 'box4' in done:
                    pygame.draw.circle(main_scren, (0, 0, 255), (250, 154), 30)
                    done.remove('box4')
                    map_t[2] = 2
                    win(map_t)
                elif map_t[1] == 2 and map_t[2] == 2 and 'box5' in done:
                    pygame.draw.circle(main_scren, (0, 0, 255), (400, 154), 30)
                    done.remove('box5')
                    map_t[3] = 2
                    win(map_t)
                elif map_t[1] == 2 and map_t[3] == 2 and 'box4' in done:
                    pygame.draw.circle(main_scren, (0, 0, 255), (100, 154), 30)
                    done.remove('box1')
                    map_t[1] = 2
                    win(map_t)
                elif map_t[1] == 2 and map_t[5] == 2 and 'box9' in done:
                    pygame.draw.circle(main_scren, (0, 0, 255), (400, 389), 30)
                    done.remove('box9')
                    map_t[9] = 2
                    win(map_t)
                elif map_t[1] == 2 and map_t[9] == 2 and 'box6' in done:
                    pygame.draw.circle(main_scren, (0, 0, 255), (250, 268), 30)
                    done.remove('box6')
                    map_t[5] = 2
                    win(map_t)
                elif map_t[1] == 2 and map_t[4] == 2 and 'box3' in done:
                    pygame.draw.circle(main_scren, (0, 0, 255), (100, 389), 30)
                    done.remove('box3')
                    map_t[7] = 2
                    win(map_t)
                elif map_t[1] == 2 and map_t[7] == 2 and 'box2' in done:
                    pygame.draw.circle(main_scren, (0, 0, 255), (100, 268), 30)
                    done.remove('box2')
                    map_t[4] = 2
                    win(map_t)
                elif map_t[2] == 2 and map_t[3] == 2 and 'box1' in done:
                    pygame.draw.circle(main_scren, (0, 0, 255), (100, 154), 30)
                    done.remove('box1')
                    map_t[1] = 2
                    win(map_t)
                elif map_t[2] == 2 and map_t[8] == 2 and 'box6' in done:
                    pygame.draw.circle(main_scren, (0, 0, 255), (250, 268), 30)
                    done.remove('box6')
                    map_t[5] = 2
                    win(map_t)

                elif map_t[3] == 2 and map_t[5] == 2 and 'box3' in done:
                    pygame.draw.circle(main_scren, (0, 0, 255), (100, 389), 30)
                    done.remove('box3')
                    map_t[7] = 2
                    win(map_t)
                elif map_t[3] == 2 and map_t[7] == 2 and 'box6' in done:
                    pygame.draw.circle(main_scren, (0, 0, 255), (250, 268), 30)
                    done.remove('box6')
                    map_t[5] = 2
                    win(map_t)
                elif map_t[3] == 2 and map_t[6] == 2 and 'box9' in done:
                    pygame.draw.circle(main_scren, (0, 0, 255), (400, 389), 30)
                    done.remove('box9')
                    map_t[9] = 2
                    win(map_t)
                elif map_t[3] == 2 and map_t[9] == 2 and 'box7' in done:
                    pygame.draw.circle(main_scren, (0, 0, 255), (400, 268), 30)
                    done.remove('box7')
                    map_t[6] = 2
                    win(map_t)
                elif map_t[4] == 2 and map_t[1] == 2 and 'box3' in done:
                    pygame.draw.circle(main_scren, (0, 0, 255), (100, 389), 30)
                    done.remove('box3')
                    map_t[9] = 2
                    win(map_t)
                elif map_t[4] == 2 and map_t[7] == 2 and 'box1' in done:
                    pygame.draw.circle(main_scren, (0, 0, 255), (100, 154), 30)
                    done.remove('box1')
                    map_t[1] = 2
                    win(map_t)
                elif map_t[4] == 2 and map_t[5] == 2 and 'box7' in done:
                    pygame.draw.circle(main_scren, (0, 0, 255), (400, 268), 30)
                    done.remove('box7')
                    map_t[6] = 2
                    win(map_t)
                elif map_t[4] == 2 and map_t[6] == 2 and 'box6' in done:
                    pygame.draw.circle(main_scren, (0, 0, 255), (250, 268), 30)
                    done.remove('box6')
                    map_t[5] = 2
                    win(map_t)
                elif map_t[5] == 2 and map_t[6] == 2 and 'box2' in done:
                    pygame.draw.circle(main_scren, (0, 0, 255), (100, 268), 30)
                    done.remove('box2')
                    map_t[4] = 2
                    win(map_t)
                elif map_t[7] == 2 and map_t[8] == 2 and 'box9' in done:
                    pygame.draw.circle(main_scren, (0, 0, 255), (400, 389), 30)
                    done.remove('box9')
                    map_t[9] = 2
                    win(map_t)
                elif map_t[7] == 1 and map_t[5] == 1 and 'box5' in done:
                    pygame.draw.circle(main_scren, (0, 0, 255), (400, 154), 30)
                    done.remove('box5')
                    map_t[3] = 2
                    win(map_t)
                elif map_t[7] == 2 and map_t[9] == 2 and 'box8' in done:
                    pygame.draw.circle(main_scren, (0, 0, 255), (250, 389), 30)
                    done.remove('box8')
                    map_t[8] = 2
                    win(map_t)

                elif map_t[8] == 2 and map_t[9] == 2 and 'box3' in done:
                    pygame.draw.circle(main_scren, (0, 0, 255), (100, 389), 30)
                    done.remove('box3')
                    map_t[7] = 2
                    win(map_t)
                elif map_t[9] == 2 and map_t[6] == 2 and 'box5' in done:
                    pygame.draw.circle(main_scren, (0, 0, 255), (400, 154), 30)
                    done.remove('box5')
                    map_t[3] = 2
                    win(map_t)
                elif map_t[9] == 2 and map_t[5] == 2 and 'box1' in done:
                    pygame.draw.circle(main_scren, (0, 0, 255), (100, 154), 30)
                    done.remove('box1')
                    map_t[1] = 2
                    win(map_t)
                elif map_t[2] == 2 and map_t[5] == 2 and 'box8' in done:
                    pygame.draw.circle(main_scren, (0, 0, 255), (250, 389), 30)
                    done.remove('box8')

                    map_t[8] = 2
                    win(map_t)
                elif map_t[8] == 2 and map_t[5] == 2 and 'box4' in done:
                    pygame.draw.circle(main_scren, (0, 0, 255), (250, 154), 30)
                    done.remove('box4')
                    map_t[2] = 2
                    win(map_t)
                ################################
                elif map_t[1] == 1 and map_t[2] == 1 and 'box5' in done:
                    pygame.draw.circle(main_scren, (0, 0, 255), (400, 154), 30)
                    done.remove('box5')
                    map_t[3] = 2
                    win(map_t)
                elif map_t[1] == 1 and map_t[3] == 1 and 'box4' in done:
                    pygame.draw.circle(main_scren, (0, 0, 255), (250, 154), 30)
                    done.remove('box4')
                    map_t[2] = 2
                    win(map_t)
                elif map_t[1] == 1 and map_t[5] == 1 and 'box9' in done:
                    pygame.draw.circle(main_scren, (0, 0, 255), (400, 389), 30)
                    done.remove('box9')
                    map_t[9] = 2
                    win(map_t)
                elif map_t[1] == 1 and map_t[9] == 1 and 'box6' in done:
                    pygame.draw.circle(main_scren, (0, 0, 255), (250, 268), 30)
                    done.remove('box6')
                    map_t[5] = 2
                    win(map_t)
                elif map_t[1] == 1 and map_t[4] == 1 and 'box3' in done:
                    pygame.draw.circle(main_scren, (0, 0, 255), (100, 389), 30)
                    done.remove('box3')
                    map_t[7] = 2
                    win(map_t)
                elif map_t[1] == 1 and map_t[7] == 1 and 'box2' in done:
                    pygame.draw.circle(main_scren, (0, 0, 255), (100, 268), 30)
                    done.remove('box2')
                    map_t[4] = 2
                    win(map_t)
                elif map_t[2] == 1 and map_t[3] == 1 and 'box1' in done:
                    pygame.draw.circle(main_scren, (0, 0, 255), (100, 154), 30)
                    done.remove('box1')
                    map_t[1] = 2
                    win(map_t)
                elif map_t[2] == 1 and map_t[8] == 1 and 'box6' in done:
                    pygame.draw.circle(main_scren, (0, 0, 255), (250, 268), 30)
                    done.remove('box6')
                    map_t[5] = 2
                    win(map_t)
                elif map_t[2] == 1 and map_t[5] == 1 and 'box8' in done:
                    pygame.draw.circle(main_scren, (0, 0, 255), (250, 389), 30)
                    done.remove('box8')
                    map_t[8] = 2
                    win(map_t)
                elif map_t[3] == 1 and map_t[5] == 1 and 'box3' in done:
                    pygame.draw.circle(main_scren, (0, 0, 255), (100, 389), 30)
                    done.remove('box3')
                    map_t[7] = 2
                    win(map_t)
                elif map_t[3] == 1 and map_t[7] == 1 and 'box6' in done:
                    pygame.draw.circle(main_scren, (0, 0, 255), (250, 268), 30)
                    done.remove('box6')
                    map_t[5] = 2
                    win(map_t)
                elif map_t[3] == 1 and map_t[6] == 1 and 'box9' in done:
                    pygame.draw.circle(main_scren, (0, 0, 255), (400, 389), 30)
                    done.remove('box9')
                    map_t[9] = 2
                    win(map_t)
                elif map_t[3] == 1 and map_t[9] == 1 and 'box7' in done:
                    pygame.draw.circle(main_scren, (0, 0, 255), (400, 268), 30)
                    done.remove('box7')
                    map_t[5] = 2
                    win(map_t)
                elif map_t[4] == 1 and map_t[7] == 1 and 'box1' in done:
                    pygame.draw.circle(main_scren, (0, 0, 255), (100, 154), 30)
                    done.remove('box1')
                    map_t[1] = 2
                    win(map_t)
                elif map_t[4] == 1 and map_t[5] == 1 and 'box7' in done:
                    pygame.draw.circle(main_scren, (0, 0, 255), (400, 268), 30)
                    done.remove('box7')
                    map_t[6] = 2
                    win(map_t)
                elif map_t[4] == 1 and map_t[6] == 1 and 'box6' in done:
                    pygame.draw.circle(main_scren, (0, 0, 255), (250, 268), 30)
                    done.remove('box6')
                    map_t[5] = 2
                    win(map_t)
                elif map_t[5] == 1 and map_t[6] == 1 and 'box2' in done:
                    pygame.draw.circle(main_scren, (0, 0, 255), (100, 268), 30)
                    done.remove('box2')
                    map_t[4] = 2
                    win(map_t)
                elif map_t[7] == 1 and map_t[8] == 1 and 'box9' in done:
                    pygame.draw.circle(main_scren, (0, 0, 255), (400, 389), 30)
                    done.remove('box9')
                    map_t[9] = 2
                    win(map_t)
                elif map_t[7] == 1 and map_t[5] == 1 and 'box5' in done:
                    pygame.draw.circle(main_scren, (0, 0, 255), (400, 154), 30)
                    done.remove('box5')
                    map_t[3] = 2
                    win(map_t)
                elif map_t[7] == 1 and map_t[9] == 1 and 'box8' in done:
                    pygame.draw.circle(main_scren, (0, 0, 255), (250, 389), 30)
                    done.remove('box8')
                    map_t[8] = 2
                    win(map_t)
                elif map_t[8] == 1 and map_t[5] == 1 and 'box4' in done:
                    pygame.draw.circle(main_scren, (0, 0, 255), (250, 154), 30)
                    done.remove('box4')
                    map_t[2] = 2
                    win(map_t)
                elif map_t[8] == 1 and map_t[9] == 1 and 'box3' in done:
                    pygame.draw.circle(main_scren, (0, 0, 255), (100, 389), 30)
                    done.remove('box3')
                    map_t[7] = 2
                    win(map_t)
                elif map_t[9] == 1 and map_t[6] == 1 and 'box5' in done:
                    pygame.draw.circle(main_scren, (0, 0, 255), (400, 154), 30)
                    done.remove('box5')
                    map_t[3] = 2
                    win(map_t)
                elif map_t[9] == 1 and map_t[5] == 1 and 'box1' in done:
                    pygame.draw.circle(main_scren, (0, 0, 255), (100, 154), 30)
                    done.remove('box1')
                    map_t[1] = 2
                    win(map_t)
                ####################################
                else:
                    if len(done) == 0:
                        run = False
                    else:
                        win(map_t)
                        box = random.choice(done)
                        if box == 'box1':
                            pygame.draw.circle(main_scren, (0, 0, 255), (100, 154), 30)
                            done.remove('box1')
                            map_t[1] = 2
                            win(map_t)
                        if box == 'box2':
                            pygame.draw.circle(main_scren, (0, 0, 255), (100, 268), 30)
                            done.remove('box2')
                            map_t[4] = 2
                            win(map_t)
                        if box == 'box3':
                            pygame.draw.circle(main_scren, (0, 0, 255), (100, 389), 30)
                            done.remove('box3')
                            map_t[7] = 2
                            win(map_t)
                        if box == 'box4':
                            pygame.draw.circle(main_scren, (0, 0, 255), (250, 154), 30)
                            done.remove('box4')
                            map_t[2] = 2
                            win(map_t)
                        if box == 'box5':
                            pygame.draw.circle(main_scren, (0, 0, 255), (400, 154), 30)
                            done.remove('box5')
                            map_t[3] = 2
                            win(map_t)
                        if box == 'box6':
                            pygame.draw.circle(main_scren, (0, 0, 255), (250, 268), 30)
                            done.remove('box6')
                            map_t[5] = 2
                            win(map_t)
                        if box == 'box7':
                            pygame.draw.circle(main_scren, (0, 0, 255), (400, 268), 30)
                            done.remove('box7')
                            map_t[6] = 2
                            win(map_t)
                        if box == 'box8':
                            pygame.draw.circle(main_scren, (0, 0, 255), (250, 389), 30)
                            done.remove('box8')
                            map_t[8] = 2
                            win(map_t)
                        if box == 'box9':
                            pygame.draw.circle(main_scren, (0, 0, 255), (400, 389), 30)
                            done.remove('box9')
                            map_t[9] = 2
                            win(map_t)
                    win(map_t)
                win(map_t)
        win(map_t)
    clock.tick(120)
    win(map_t)
    pygame.display.update()