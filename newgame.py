import random
import tkinter as tk
import pyttsx3
from PIL import ImageTk,Image

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def start_game():
    global im
    global b1,b2
    # Button for players

    # button for player1
    b1.place(x=1200, y=400)
    # button for player2
    b2.place(x=1200, y=550)

    # Dice
    im = Image.open("dice.jpeg")
    im = im.resize((65, 65))
    im = ImageTk.PhotoImage(im)
    b4 = tk.Button(root, image=im, height=80, width=80)
    b4.place(x=1200, y=150)

    # exitbutton
    b3 = tk.Button(root, text="Click here to End Game", height=3, width=20, fg="red", bg="yellow",
                   font=('Cursive', 16, 'bold'), activebackground='red',command=reset_coins)
    b3.place(x=1200, y=20)

def reset_coins():
    global player1,player2
    global pos1,pos2
    player1.place(x=1100, y=420)
    player2.place(x=1100, y=570)
    pos1=0
    pos2=0

def load_dice_images():
    global Dice
    names = ["d1.png", "d2.png", "d3.png", "d4.png", "d5.png", "d6.jpeg"]
    for i in names:
        im = Image.open(""+i)
        im = im.resize((65, 65))
        im = ImageTk.PhotoImage(im)
        Dice.append(im)

def roll_dice1():
    global Dice
    global r,s
    global pos1,pos2
    global b1,b2
    r=random.randint(1,6)
    b5=tk.Button(root,image=Dice[r-1],height=80,width=80)
    b5.place(x=1200,y=150)
    speak(r)

    if r>s:
        pos1=pos1+r
        move_coin1(r)
    b1.configure('disabled')

    is_winner()

def roll_dice2():
    global Dice
    global r, s
    global pos1, pos2
    global b1, b2
    s = random.randint(1, 6)
    b6 = tk.Button(root, image=Dice[s - 1], height=80, width=80)
    b6.place(x=1400, y=150)
    speak(s)
    if r<s:
        pos2=pos2+s
        move_coin2(s)

    is_winner()

def is_winner():
    global pos1,pos2
    if pos1==100:
        speak("player1 is the winner")
        msg="PLAYER-1 is the WINNER"
        Lab=tk.Label(root,text=msg,height=2,width=20,bg='red',font=('Cursive',30,'bold'))
        Lab.place(x=300,y=300)
        reset_coins()
    elif pos2==100:
        speak("player2 is the winner")
        msg="PLAYER-2 is the WINNER"
        Lab=tk.Label(root,text=msg,height=2,width=20,bg='red',font=('Cursive',30,'bold'))
        Lab.place(x=300,y=300)
        reset_coins()


def move_coin1(r):
    global player1,player2
    global Index
    global s
    global pos1, pos2
    if r>s:
        player1.place(x=Index[pos1][0],y=Index[pos1][1])


def move_coin2(s):
    global player1,player2
    global Index
    global r
    global pos1, pos2
    if r<s:
        player2.place(x=Index[pos2][0], y=Index[pos2][1])






def get_Index():
    global player1,player2
    Num=[100,99,98,978,96,95,94,93,92,91,81,82,83,84,85,86,87,88,89,90,80,79,78,77,76,75,74,73,72,71,61,62,63,64,65,66,67,68,69,70,60,59,58,57,56,55,54,53,52,51,41,42,43,44,45,46,47,48,49,50,40,39,38,37,36,35,34,33,32,31,21,22,23,24,25,26,27,28,29,30,20,19,18,17,16,15,14,13,12,11,1,2,3,4,5,6,7,8,9,10]
    #player1.place(x=100,y=20)
    row=20
    i=0
    for x in range(1,11):
        col=100
        for y in range (1,11):
            Index[Num[i]]=(col,row)
            col=col+80
            i=i+1
        row=row+80
    print(Index)

#to store dice images
Dice=[]

#to store x and y coordinates of given num
Index={}

#initial position of players
pos1=None
pos2=None


root=tk.Tk()
root.geometry("1200x800")
root.title("ChaseMe")

#Board
f1=tk.Frame(root,width=1200,height=800,relief='raised')
f1.place(x=80,y=-10)
img1=ImageTk.PhotoImage(Image.open("1.png"))
Lab=tk.Label(f1,image=img1)
Lab.place(x=0,y=0)

#dice1
r=random.randint(1,6)
#dice2
s=random.randint(1,6)

#player1 button
b1 = tk.Button(root, text="Player-1", height=3, width=20, fg="red", bg="cyan", font=('Cursive', 16, 'bold'),
               activebackground='green', command=roll_dice1)
#player2 button
b2 = tk.Button(root, text="Player-2", height=3, width=20, fg="red", bg="orange", font=('Cursive', 16, 'bold'),
               activebackground='green', command=roll_dice2)


#player1 coin
player1=tk.Canvas(root,width=40,height=40)
player1.create_oval(10,10,40,40,fill='cyan')

#player2 coin
player2=tk.Canvas(root,width=40,height=40)
player2.create_oval(10,10,40,40,fill='orange')

#whose turn first...by default player1
turn=1

#keep coins at initial position
reset_coins()

#indexing of all the players
get_Index()

#Load dice images
load_dice_images()

#setting all the buttons
start_game()
root.mainloop()
