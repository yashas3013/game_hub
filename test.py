import pygame, random

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
done = []
map_t = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0}


def win_screen1():
    global run
    base_font = pygame.font.Font(None, 60)
    text = 'RED WINS'
    surface = base_font.render(text, True, (255, 0, 0))
    main_scren.blit(surface, (210, 45))



def win_screen2():
    global run
    main_scren.fill((0, 0, 0))
    base_font = pygame.font.Font(None, 60)
    text = 'BLUE WINS'
    surface = base_font.render(text, True, (0, 0, 255))
    main_scren.blit(surface, (210, 45))



while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONUP:
            mouse = pygame.mouse.get_pos()
            # print(mouse)
            if box1.collidepoint(mouse) and 'box1' not in done:
                if object_state == 0:
                    pygame.draw.rect(main_scren, colour1, (60, 112, 80, 80))
                    done.append('box1')
                    map_t[1] = 1
                    object_state = 1
                else:
                    pygame.draw.circle(main_scren, (0, 0, 255), (100, 154), 30)
                    object_state = 0
                    done.append('box1')
                    map_t[1] = 2
            if box2.collidepoint(mouse) and 'box2' not in done:
                if object_state == 0:
                    pygame.draw.rect(main_scren, colour1, (60, 232, 80, 80))
                    object_state = 1
                    done.append('box2')
                    map_t[4] = 1
                else:
                    pygame.draw.circle(main_scren, (0, 0, 255), (100, 268), 30)
                    object_state = 0
                    done.append('box2')
                    map_t[4] = 2
            if box3.collidepoint(mouse) and 'box3' not in done:
                if object_state == 0:
                    pygame.draw.rect(main_scren, colour1, (60, 352, 80, 80))
                    object_state = 1
                    done.append('box3')
                    map_t[7] = 1
                else:
                    pygame.draw.circle(main_scren, (0, 0, 255), (100, 389), 30)
                    object_state = 0
                    done.append('box3')
                    map_t[7] = 2
            if box4.collidepoint(mouse) and 'box4' not in done:
                if object_state == 0:
                    pygame.draw.rect(main_scren, colour1, (212, 112, 80, 80))
                    object_state = 1
                    done.append('box4')
                    map_t[2] = 1
                else:
                    pygame.draw.circle(main_scren, (0, 0, 255), (250, 154), 30)
                    object_state = 0
                    done.append('box4')
                    map_t[2] = 2
            if box5.collidepoint(mouse) and 'box5' not in done:
                if object_state == 0:
                    pygame.draw.rect(main_scren, colour1, (360, 112, 80, 80))
                    object_state = 1
                    done.append('box5')
                    map_t[3] = 1
                else:
                    pygame.draw.circle(main_scren, (0, 0, 255), (400, 154), 30)
                    object_state = 0
                    done.append('box5')
                    map_t[3] = 2
            if box6.collidepoint(mouse) and 'box6' not in done:
                if object_state == 0:
                    pygame.draw.rect(main_scren, colour1, (212, 232, 80, 80))
                    object_state = 1
                    done.append('box6')
                    map_t[5] = 1
                else:
                    pygame.draw.circle(main_scren, (0, 0, 255), (250, 268), 30)
                    object_state = 0
                    done.append('box6')
                    map_t[5] = 2
            if box7.collidepoint(mouse) and 'box7' not in done:
                if object_state == 0:
                    pygame.draw.rect(main_scren, colour1, (360, 232, 80, 80))
                    object_state = 1
                    done.append('box7')
                    map_t[6] = 1
                else:
                    pygame.draw.circle(main_scren, (0, 0, 255), (400, 268), 30)
                    object_state = 0
                    done.append('box7')
                    map_t[6] = 2
            if box8.collidepoint(mouse) and 'box8' not in done:
                if object_state == 0:
                    pygame.draw.rect(main_scren, colour1, (212, 352, 80, 80))
                    object_state = 1
                    done.append('box8')
                    map_t[8] = 1
                else:
                    pygame.draw.circle(main_scren, (0, 0, 255), (250, 389), 30)
                    object_state = 0
                    done.append('box8')
                    map_t[8] = 2
            if box9.collidepoint(mouse) and 'box9' not in done:
                if object_state == 0:
                    pygame.draw.rect(main_scren, colour1, (360, 352, 80, 80))
                    object_state = 1
                    done.append('box9')
                    map_t[9] = 1
                else:
                    pygame.draw.circle(main_scren, (0, 0, 255), (400, 389), 30)
                    object_state = 0
                    done.append('box9')
                    map_t[9] = 2

            if map_t[1] == 1 and map_t[2] == 1 and map_t[3] == 1:
                win_screen1()
            if map_t[1] == 2 and map_t[2] == 2 and map_t[3] == 2:
                win_screen2()
            if map_t[1] == 1 and map_t[4] == 1 and map_t[7] == 1:
                win_screen1()
            if map_t[1] == 2 and map_t[4] == 2 and map_t[7] == 2:
                win_screen2()
            if map_t[1] == 1 and map_t[5] == 1 and map_t[9] == 1:
                win_screen1()
            if map_t[1] == 2 and map_t[5] == 2 and map_t[9] == 2:
                win_screen2()
            if map_t[3] == 1 and map_t[5] == 1 and map_t[7] == 1:
                win_screen1()
            if map_t[3] == 2 and map_t[5] == 2 and map_t[7] == 2:
                win_screen2()
            if map_t[4] == 1 and map_t[5] == 1 and map_t[6] == 1:
                win_screen1()
            if map_t[4] == 2 and map_t[5] == 2 and map_t[6] == 2:
                win_screen2()
            if map_t[7] == 1 and map_t[8] == 1 and map_t[9] == 1:
                win_screen1()
            if map_t[7] == 2 and map_t[6] == 2 and map_t[9] == 2:
                win_screen2()
            if map_t[2] == 1 and map_t[5] == 1 and map_t[8] == 1:
                win_screen1()
            if map_t[2] == 2 and map_t[5] == 2 and map_t[8] == 2:
                win_screen2()
            if map_t[3] == 1 and map_t[6] == 1 and map_t[9] == 1:
                win_screen1()
            if map_t[3] == 2 and map_t[6] == 2 and map_t[9] == 2:
                win_screen2()
    pygame.display.update()
