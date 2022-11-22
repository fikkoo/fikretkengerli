
from tkinter.messagebox import *
from tkinter import *


root = Tk()
root.resizable(False,False)
root.title('Noughts and Crosses')
root.geometry("400x330")

"""from PIL import Image, ImageTk

icon = Image.open("C:\\Users\\user\\Desktop\\download.png")
photo = ImageTk.PhotoImage(icon)
root.wm_iconphoto(False,photo)"""


x_wins = 0
o_wins = 0
all_games = 1
no_one_wins = 0

move = True


arr = []

list1 = ["n"]


def new_game():
    for row in range(3):
        for col in range(3):
            arr[row][col]['text'] = ' '
            global list1
            list1 = ["n"]
            arr[row][col]['background'] = 'white'
    global all_games
    all_games += 1
    winner_x["text"] = " "
    winner_o["text"] = " "
    winner_no["text"] = " "
    label["text"] = " "
    global move
    move = True
    global no_win
    no_win = True
    global  no_one_wins



label = Label(root, text = " ", font = "Helvetica 10")
label.place(x=15, y= 300)

goal = Label(text = "Enter the number of games:")
goal.place(x=239, y=100)
entry = Entry(root)
entry.place(x=250, y=120)
goal_label = Label(root, text = " ")
goal_label.place(x=250, y=180)

def ok_btn():
    global all_games
    global x_wins
    global o_wins
    all_games = 1
    x_wins = 0
    o_wins = 0
    if entry.get() == "" :
        showwarning(title="Attention!" ,message = "You didn't enter anything! Enter a number and try again!")
        entry.delete(0,END)
    else:
        e = int(entry.get())
        goal_label["text"] = f"You will play: {e} games"
        result_btn.config(state = NORMAL)

ok = Button(root, text = "Ok", command = ok_btn)
ok.place(x=250, y=140)


def creat_window_for_x():
    global goal_label
    goal_label["text"] = " "
    window = Tk()
    window.title("The Winner")
    def quit_btn():
        window.destroy()
    window.geometry("260x100")
    window_label = Label(window, text="X won! Congratulations!", font='Helvetica 15', fg="Green")
    quit_window = Button(window, text="Quit", bg="white", fg="black", command=quit_btn)
    quit_window.place(x=200, y=70)
    window_label.pack()
    window.mainloop()

def creat_window_for_o():
    global goal_label
    goal_label["text"] = " "
    window = Tk()
    window.title("The Winner")
    def quit_btn():
        window.destroy()
    window.geometry("260x100")
    window_label = Label(window, text="O won! Congratulations!", font='Helvetica 15', fg="Green")
    quit_window = Button(window, text="Quit", bg="white", fg="black", command=quit_btn)
    quit_window.place(x=200, y=70)
    window_label.pack()
    window.mainloop()

def creat_no_one_wins():
    global goal_label
    goal_label["text"] = " "
    window = Tk()
    window.title("Draw")
    def quit_btn():
        window.destroy()
    window.geometry("260x100")
    window_label = Label(window, text="Draw", font='Helvetica 15', fg="red")
    quit_window = Button(window, text="Quit", bg="white", fg="black", command=quit_btn)
    quit_window.place(x=200, y=70)
    window_label.pack()
    window.mainloop()

def result():
    if all_games == int(entry.get()):
        if x_wins > o_wins:
            creat_window_for_x()
        if x_wins < o_wins:
            creat_window_for_o()
        if x_wins == o_wins:
            creat_no_one_wins()
    if all_games != int(entry.get()):
        showinfo(title="Warning!", message = 'The number of your games is not equal to the given one!')

result_btn = Button(root, text = "Result",bg = "grey", fg = "white", command = result)
result_btn.place(x=169, y=270)
result_btn.config(state = DISABLED)

no_win = True

def x_or_o(row, col):
    if move == True:
        if arr[row][col]['text'] == ' ':
            label["text"] = " "
            if len(list1) % 2 != 0:
                arr[row][col]['text'] = 'X'
                list1.append("n")
                check_win()
                if no_win == True:
                    nichya()

            else:
                arr[row][col]['text'] = 'O'
                check_win()
                list1.append("n")
        else:
            label["text"] = "You can't enter there!"
    else:    
        label["text"] = "Game over! Please start again!"

winner_x = Label(root, text = " ")
winner_x.place(x=270, y = 200)

winner_o = Label(root, text = " ")
winner_o.place(x=270, y = 200)

winner_no = Label(root, text = " ")
winner_no.place(x=270, y = 200)

def check_win():
    global x_wins
    global o_wins
    global winner_no
    global winner_x
    global winner_o
    global move
    global no_win
    for n in range(3):
        if arr[n][0]['text'] == "X" and arr[n][1]['text'] == "X" and arr[n][2]['text'] == "X":
            x_wins += 1
            move = False
            no_win = False
            arr[n][0]["background"] = arr[n][1]["background"] = arr[n][2]["background"] = "light blue"
            winner_x["text"] = "X won"


        if arr[0][n]["text"] == "X" and arr[1][n]["text"] == "X" and arr[2][n]["text"] == "X":
            x_wins += 1
            move = False
            no_win = False
            arr[0][n]["background"] = arr[1][n]["background"] = arr[2][n]["background"] = "light blue"
            winner_x["text"] = "X won"

    if arr[0][0]["text"] == "X" and arr[1][1]["text"] == "X" and arr[2][2]["text"] == "X":
        x_wins += 1
        move = False
        no_win = False
        arr[0][0]["background"] = arr[1][1]["background"] = arr[2][2]["background"] = "light blue"
        winner_x["text"] = "X won"

    if arr[2][0]["text"] == "X" and arr[1][1]["text"] == "X" and arr[0][2]["text"] == "X":
        x_wins += 1
        move = False
        no_win = False
        arr[2][0]["background"] = arr[1][1]["background"] = arr[0][2]["background"] = "light blue"
        winner_x["text"] = "X won"

    for n in range(3):
        if arr[n][0]["text"] == "O" and arr[n][1]["text"] == "O" and arr[n][2]["text"] == "O":
            arr[n][0]["background"] = arr[n][1]["background"] = arr[n][2]["background"] = "light blue"
            o_wins += 1
            move = False
            no_win = False
            winner_o["text"] = "O won"

        if arr[0][n]["text"] == "O" and arr[1][n]["text"] == "O" and arr[2][n]["text"] == "O":
            arr[0][n]["background"] = arr[1][n]["background"] = arr[2][n]["background"] = "light blue"
            o_wins += 1
            move = False
            no_win = False
            winner_o["text"] = "O won"

    if arr[0][0]["text"] == "O" and arr[1][1]["text"] == "O" and arr[2][2]["text"] == "O":
        arr[0][0]["background"] = arr[1][1]["background"] = arr[2][2]["background"] = "light blue"
        o_wins += 1
        move = False
        no_win = False
        winner_o["text"] = "O won"


    if arr[2][0]["text"] == "O" and arr[1][1]["text"] == "O" and arr[0][2]["text"] == "O":
        arr[2][0]["background"] = arr[1][1]["background"] = arr[0][2]["background"] = "light blue"
        o_wins += 1
        move = False
        no_win = False
        winner_o["text"] = "O won"

def nichya():
    global move
    global no_win
    no_win = True

    for n in range(3):
        if arr[n][0]['text'] != " " and arr[n][1]['text'] != " " and arr[n][2]['text'] != " " \
            and arr[0][n]["text"] != " " and arr[1][n]["text"] != " " and arr[2][n]["text"] != " " \
            and arr[0][0]["text"] != " " and arr[1][1]["text"] != " " and arr[2][2]["text"] != " " \
            and arr[2][0]["text"] != " " and arr[1][1]["text"] != " " and arr[0][2]["text"] != " ":
            winner_no["text"] = "Draw"
            move = False
            arr[n][0]['background'] = arr[n][1]['background'] = arr[n][2]['background'] =  \
            arr[0][n]["background"] = arr[1][n]["background"] = arr[2][n]["background"] = \
            arr[0][0]["background"] = arr[1][1]["background"] = arr[2][2]["background"] =  \
            arr[2][0]["background"] = arr[1][1]["background"] = arr[0][2]["background"] = "light green"


for row in range(3):
    list = []
    for col in range(3):
        button = Button(root, text=" ", width=4, height=2,  font= 'Helvetica 20 bold', bg ='white',
                        command = lambda row=row, col=col: x_or_o(row,col))
        button.grid(row=row, column=col)
        list.append(button)
    arr.append(list)


def clear_st():
    global all_games
    global x_wins
    global o_wins
    new_game()
    all_games = 1
    x_wins = 0
    o_wins = 0
    statistics = Label(root, text=f"       Games: {all_games}\nX wins: {x_wins}\nO wins: {o_wins}\n   Draws: {all_games - x_wins - o_wins}", font = "Helvetica 10")
    statistics.place(x=250, y=1)

def statistics():
    statistics = Label(root, text=f"       Games: {all_games}\nX wins: {x_wins}\nO wins: {o_wins}\n   Draws: {all_games - x_wins - o_wins}", font = "Helvetica 10")
    statistics.place(x=250, y=1)
    stat_btn["text"] = "Обновить"
    clear_btn = Button(root, text='Очистить', font="Helvetica 8", command= clear_st)
    clear_btn.place(x=250, y=70)

def close():
    root.destroy()

created = Label(root, text = "©Fikret Kengerli")
created.place(x = 305, y = 308)

stat_btn = Button(root, text = 'Statistics', bg = "grey", fg = "white",command = statistics)
stat_btn.place(x=85, y=270)

new_button = Button(root, text = 'New game', command=new_game, bg = "grey", fg = "white")
new_button.place(x=5, y=270)
new_button.config(state = NORMAL)

close_btn = Button(root, text = 'Close', command = close, bg = "dark red", fg = "white")
close_btn.place(x = 305, y = 250)

root.mainloop()
