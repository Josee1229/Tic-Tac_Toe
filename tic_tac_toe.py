# Building Tic Tac Toe game using Python and Tkinter

import tkinter as tk

root = tk.Tk()
root.geometry("500x500")
root.title("Tic Tac Toe")
root.configure(bg='pink')

frame1 = tk.Frame(root)
frame1.pack()
titleLabel = tk.Label(frame1, text = "Tic Tac Toe", font=("Montserrat", 25), bg="pink", fg="#ff3d3e",width=20)
titleLabel.grid(row=0, column=0)

frame2 = tk.Frame(root)
frame2.pack()

board = {1:" ", 2:" ", 3:" ",
        4:" ", 5:" ", 6:" ",
        7:" ", 8:" ", 9:" "
         }

turn = 'x'
game_end = False

def checkForWin(player):
    if (board[1] == board[2] and board[2] == board[3] and board[3] == player):
        return True
    elif (board[4] == board[5] and board[5] == board[6] and board[6] == player):
        return True
    elif (board[7] == board[8] and board[8] == board[9] and board[9] == player):
        return True
    elif (board[1] == board[4] and board[4] == board[7] and board[7] == player):
        return True
    elif (board[2] == board[5] and board[5] == board[8] and board[8] == player):
        return True
    elif (board[3] == board[6] and board[6] == board[9] and board[9] == player):
        return True
    elif (board[1] == board[5] and board[5] == board[9] and board[9] == player):
        return True
    elif (board[3] == board[5] and board[5] == board[7] and board[7] == player):
        return True
    else:
        return False;


def checkForDraw():
    for i in board.keys():
        if board[i] == ' ':
            return False
    return True




def play(event):
    global turn,game_end
    button = event.widget

    buttonTxt = str(button)
    buttonIdentifier = buttonTxt[-1]
    if buttonIdentifier == 'n':
        clicked = 1
    else:
        clicked = int(buttonIdentifier)



    if button["text"] == " " and game_end==False:
        if turn == 'x':
            button["text"] = 'x'
            board[clicked] = turn
            if checkForWin(turn):
                winningLabel = tk.Label(frame1, text=f"{turn} wins the game!",font=('Montserrat',25),bg='pink',fg='#ff3d3e', width=20)
                winningLabel.grid(row=0,column=0,columnspan=3)
                game_end = True
            turn = 'o'
        else:
            button["text"] = 'o'
            board[clicked] = turn
            if checkForWin(turn):
                winningLabel = tk.Label(frame1, text=f"{turn} wins the game!",font=('Montserrat',25),bg='pink',fg='#ff3d3e', width=20)
                winningLabel.grid(row=0, column=0, columnspan=3)
                game_end = True
            turn = 'x'

        if checkForDraw():
            drawLabel = tk.Label(frame1, text="Game Draw!", font=('Montserrat', 25), bg='pink',fg='#ff3d3e', width=20)
            drawLabel.grid(row=0, column=0)



# Tic-tac-toe Board Creation

#1st row
button1 = tk.Button(frame2, text = " ", width = 4, height = 2,font = ("Montserrat",30),bg="green", relief=tk.RAISED, borderwidth=5)
button1.grid(row = 0, column = 0)
button1.bind("<Button-1>", play)

button2 = tk.Button(frame2, text = " ", width = 4, height = 2,font = ("Montserrat",30),bg="green", relief=tk.RAISED, borderwidth=5)
button2.grid(row = 0, column = 1)
button2.bind("<Button-1>", play)

button3 = tk.Button(frame2, text = " ", width = 4, height = 2,font = ("Montserrat",30),bg="green", relief=tk.RAISED, borderwidth=5)
button3.grid(row = 0, column = 2)
button3.bind("<Button-1>", play)

#2nd row
button4 = tk.Button(frame2, text = " ", width = 4, height = 2,font = ("Montserrat",30),bg="green", relief=tk.RAISED, borderwidth=5)
button4.grid(row = 1, column = 0)
button4.bind("<Button-1>", play)

button5 = tk.Button(frame2, text = " ", width = 4, height = 2,font = ("Montserrat",30),bg="green", relief=tk.RAISED, borderwidth=5)
button5.grid(row = 1, column = 1)
button5.bind("<Button-1>", play)

button6 = tk.Button(frame2, text = " ", width = 4, height = 2,font = ("Montserrat",30),bg="green", relief=tk.RAISED, borderwidth=5)
button6.grid(row = 1, column = 2)
button6.bind("<Button-1>", play)

#3rd row
button7 = tk.Button(frame2, text = " ", width = 4, height = 2,font = ("Montserrat",30),bg="green", relief=tk.RAISED, borderwidth=5)
button7.grid(row = 3, column = 0)
button7.bind("<Button-1>", play)

button8 = tk.Button(frame2, text = " ", width = 4, height = 2,font = ("Montserrat",30),bg="green", relief=tk.RAISED, borderwidth=5)
button8.grid(row = 3, column = 1)
button8.bind("<Button-1>", play)

button9 = tk.Button(frame2, text = " ", width = 4, height = 2,font = ("Montserrat",30),bg="green", relief=tk.RAISED, borderwidth=5)
button9.grid(row = 3, column = 2)
button9.bind("<Button-1>", play)



buttons = [button1,button2,button3,button4,button5,button6,button7,button8,button9]

def restartGame():
    for button in buttons:
        button['text'] = " "
    for i in board.keys():
        board[i] = " "
    titleLabel = tk.Label(frame1, text="Tic Tac Toe", font=("Montserrat", 25), bg="pink", fg="#ff3d3e", width=20)
    titleLabel.grid(row=0, column=0)
    globals()['game_end'] = False

restartButton = tk.Button(frame2, text="Restart Game", width=20, height=1, font=("Montserrat",20),bg="green", relief=tk.RAISED, borderwidth=5,command=restartGame)
restartButton.grid(row = 4, column = 0,columnspan = 3)


root.mainloop()