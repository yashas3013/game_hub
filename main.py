import os
from tkinter import *
import tkinter.font as font
import sqlite3


conn = sqlite3.connect('database.db')
cursor = conn.cursor()
user_list1 = []
padx = 0.5
pady = 0.5
button_click = True
root = Tk()
root.config(bg='orange')
root.geometry('800x600')
root.title('GAME HUB')
font1 = font.Font(family='Bauhaus 93', size=20)
font2 = font.Font(family='Bauhaus 93', size=15)
font3 = font.Font(family='Bauhaus 93', size=70, underline=True)
font4 = font.Font(family='Bauhaus 93', size=70, underline=False)
font5 = font.Font(family='Bauhaus 93', size=40, underline=True)
p = PhotoImage(file='game_controller.png')
root.iconphoto(False, p)
blue = 'black'
white = 'white'
green = 'green'
yellow = 'yellow'
orange = 'orange'
width = 30
score1 = 0
score2 = 0
score3 = 0


def motion(event):
    x, y = event.x, event.y
    print('{}, {}'.format(x, y))

# root.bind('<Motion>', motion)

def tictactoe_score():
    try:
        id = user_entry.get()
        cursor.execute('select tictactoe from score')
        score = cursor.fetchall()
        score = score[0][0][0]
        text = 'update playerinfo set tictactoe = ? where user_name = ? '
        cursor.execute(text, (score, id))
        conn.commit()
    except:
        id = user_entry.get()
        score = 0
        text = 'update playerinfo set tictactoe = ? where user_name = ? '
        cursor.execute(text, (score, id))
        conn.commit()


def poi_score():
    try:
        id = user_entry.get()
        cursor.execute('select poi from score')
        score = cursor.fetchall()
        score = score[0][0]
        text = 'update playerinfo set poi = ? where user_name = ? '
        cursor.execute(text, (score, id))
        conn.commit()
    except:
        id = user_entry.get()
        score = 0
        text = 'update playerinfo set poi = ? where user_name = ? '
        cursor.execute(text, (score, id))
        conn.commit()


def win(title):
    global cursor
    id = user_entry.get()
    window = Toplevel(root)
    window.title(title)
    window.geometry('436x425')
    window.config(bg=blue)
    gameover_label = Label(window, text='GAME OVER', font=font5, fg='yellow', bg=blue)
    id = user_entry.get()
    id = id.strip()
    if title == 'spacewars':
        text1 = "select spacewars from playerinfo where user_name = ?"
    elif title == 'poi':
        text1 = "select poi from playerinfo where user_name = ?"
    elif title ==  'tictactoe':
        score = score3
        text1 = "select tictactoe from playerinfo where user_name = ?"
    cursor.execute(text1, (id,))
    score1 = cursor.fetchall()
    score1 = score1[0][0]
    score1 = str(score1)     
    score_label = Label(window, text='your score: ' + str(score1), font=font2, fg=yellow, bg=blue)
    gameover_label.place(x=80, y=150)
    score_label.place(x=160, y=222)

def space():
    username=user_entry.get()
    text = 'python spacewars.py ' + username
    os.system(text)
    win('spacewars')


def tic_tac_toe1():
    os.system('python test.py')


def poi():
    username = user_entry.get()
    text = 'python poi.py ' + username
    os.system(text)
    win('poi')

def tic_tac_toe2():
    username = user_entry.get()
    text = 'python tic2.py ' + username
    os.system(text)
    win('tictactoe')


def make_userlist(user_list):
    for i in range(len(user_list)):
        user_list1.append(user_list[i][0])
    return user_list1


def check_login():
    cursor.execute('select user_name from playerinfo')
    user_list = cursor.fetchall()
    user_list = make_userlist(user_list)
    user_name = str(user_entry.get())
    user_name = user_name.strip()
    entered_name = user_name
    string1 = 'select user_password from playerinfo where user_name = ?'

    if entered_name in user_list:
        cursor.execute(string1, (entered_name,))
        correct_psw = cursor.fetchall()
        entered_psw = password_entry.get()
        entered_psw = entered_psw.strip()
        if entered_psw == str(correct_psw[0][0]):
            game_list()
        else:
            user_entry.delete(0, END)
            password_entry.delete(0, END)
            user_entry.insert(0, 'incorrect password')
    else:
        user_entry.delete(0, END)
        user_entry.insert(0, 'incorrect username')


def main_screenback1():
    user_entry.place_forget()
    password_entry.place_forget()
    password_label.place_forget()
    user_label.place_forget()
    enterbutton.place_forget()
    backbutton1.place_forget()
    main_screen()


def main_screenback2():
    user_entry.place_forget()
    password_entry1.place_forget()
    password_label.place_forget()
    user_label.place_forget()
    enterbutton1.place_forget()
    backbutton2.place_forget()
    main_screen()


def login_click():
    loginbutton.place_forget()
    registerbutton.place_forget()

    user_entry.place(x=345, y=320)
    password_entry.place(x=345, y=380)

    password_label.place(x=245, y=375)
    user_label.place(x=230, y=310)

    enterbutton.place(x=400, y=420)
    backbutton1.place(x=10, y=10)


def game_list():
    global score1,score2,score3
    registerbutton.place_forget()
    loginbutton.place_forget()
    user_entry.place_forget()
    password_entry.place_forget()
    password_label.place_forget()
    user_label.place_forget()
    enterbutton.place_forget()
    backbutton1.place_forget()
    id = user_entry.get()
    id = id.strip()
    text1 = "select spacewars from playerinfo where user_name = ?"
    cursor.execute(text1, (id,))
    score1 = cursor.fetchall()
    score1 = score1[0][0]
    score1 = str(score1)
    game1_label = Label(root, text=score1, font=font2, bg=orange, fg=blue)
    ######
    text2 = "select poi from playerinfo where user_name = ?"
    cursor.execute(text2, (id,))
    score2 = cursor.fetchall()
    score2 = score2[0][0]
    score2 = str(score2)
    game4_label = Label(root, text=score2, font=font2, bg=orange, fg=blue)
    ######
    text3 = "select tictactoe from playerinfo where user_name = ?"
    cursor.execute(text3, (id,))
    score1 = cursor.fetchall()
    score1 = score1[0][0]
    score1 = str(score1)
    game3_label = Label(root, text=score1, font=font2, bg=orange, fg=blue)
    #####
    game_label = Label(root, text='GAMES', font=font1, bg=orange, fg=blue)
    score_label = Label(root, text='SCORE', font=font1, bg=orange, fg=blue)
    refresh_button = Button(root, text='Refresh score', fg=yellow, bg=blue, font=font2, width=10, command=game_list)
    game2_label = Label(root, text='-', font=font2, bg=orange, fg=blue)
    refresh_button.place(x=0, y=0)
    game2_label.place(x=645, y=320)
    score_label.place(x=625, y=150)
    game_label.place(x=230, y=150)
    game1_label.place(x=645, y=225)
    game3_label.place(x=645, y=425)
    game4_label.place(x=645, y=525)
    game1_button.place(x=100, y=225)
    game2_button.place(x=100, y=320)
    game3_button.place(x=100, y=425)
    game4_button.place(x=100, y=525)
    game_labell.place(x=200, y=20)




def main_screen():
    loginbutton.place(x=427, y=328)
    registerbutton.place(x=210, y=328)


def hover():
    label2 = Label(root, text='', width=20, height=15)
    label2.place(x=8000, y=20)


def register_click():
    loginbutton.place_forget()
    registerbutton.place_forget()
    user_entry.place(x=345, y=320)
    password_entry1.place(x=345, y=380)
    password_label.place(x=245, y=375)
    user_label.place(x=230, y=310)
    enterbutton1.place(x=400, y=480)
    backbutton2.place(x=10, y=10)


def register_enter():
    try:
        user_name = user_entry.get()
        user_name = user_name.strip()
        user_password = password_entry1.get()
        user_password = user_password.strip()
        string = 'insert into playerinfo values(?,?,0,0,0)'
        cursor.execute(string, (user_name, user_password))
        user_entry.place_forget()
        password_entry1.place_forget()
        password_label.place_forget()
        user_label.place_forget()
        enterbutton1.place_forget()
        backbutton2.place_forget()
        loginbutton.place(x=345, y=320)
        cursor.execute('update score set spacewars = 0,poi=0,tictactoe=0; ')
        conn.commit()
    except:
        user_entry.delete(0, END)
        user_entry.insert(0, 'this username is taken,pls try again or entered psw is incorrect format')


user_entry = Entry(root, width=35)
password_entry = Entry(root, width=35, show='*')
password_entry1 = Entry(root, width=35)
password_entry2 = Entry(root, width=35)
loginbutton = Button(root, text='    LOGIN!   ', width=10, fg=yellow, bg=blue, font=font1, padx=padx, pady=pady,
                     command=login_click)

game_labell = Label(root, text='GAME HUB', fg='black', bg=orange, font=font3)
game_labell.place(x=150, y=50)
user_label = Label(root, text='UserName:', font=font2, bg=orange, fg='black')
password_label1 = Label(root, text='CONFIRM PSW', font=font2, bg=orange, fg=blue)
password_label = Label(root, text='Password:', font=font2, bg=orange, fg=blue)
registerbutton = Button(root, text='REGISTER!', fg=yellow, width=10, bg=blue, font=font1, padx=0.5, pady=0.5,
                        command=register_click)
password_entry1.insert(0, 'numerical password')
enterbutton1 = Button(root, text='REGISTER', fg=yellow, bg=blue, font=font2, command=register_enter)
enterbutton = Button(root, text='LOGIN', fg=yellow, bg=blue, font=font2, command=check_login)
backbutton1 = Button(root, text='BACK', fg=yellow, bg=blue, font=font2, command=main_screenback1)
backbutton2 = Button(root, text='BACK', fg=yellow, bg=blue, font=font2, command=main_screenback2)

game1_button = Button(root, text='SpaceWars', fg=yellow, bg=blue, font=font2, width=width, command=space)
game2_button = Button(root, text='TIC TAC TOE(MULTI PLAYER)', fg=yellow, bg=blue, width=width, font=font2,
                      command=tic_tac_toe1)
game3_button = Button(root, text='TIC TAC TOE(AI)', fg=yellow, bg=blue, font=font2, width=width, command=tic_tac_toe2)
game4_button = Button(root, text='Poi', fg=yellow, bg=blue, font=font2, width=width, command=poi)

main_screen()
root.mainloop()