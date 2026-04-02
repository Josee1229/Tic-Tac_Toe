# Building Tic Tac Toe game using Python and Tkinter

import tkinter as tk

root = tk.Tk()
root.geometry("500x500")
root.title("Tic Tac Toe")

frame1 = tk.Frame(root)
frame1.pack()
titleLabel = tk.Label(frame1, text = "Tic Tac Toe", font=("Montserrat", 25), bg="pink", fg="green")
titleLabel.pack()

frame2 = tk.Frame(root)
frame2.pack()

turn = 'x'

def play(event):
    global turn
    button = event.widget
    if turn == 'x':
        button["text"] = 'x'
        turn = 'o'
    else:
        button["text"] = 'o'
        turn = 'x'


# Tic-tac-toe Board Creation

#1st row
button1 = tk.Button(frame2, text = " ", width = 4, height = 2,font = ("Montserrat",30),bg="green", relief=tk.RAISED, borderwidth=5)
button1.grid(row = 0, column = 0)
button1.bind("<Button-1>", play)

button1 = tk.Button(frame2, text = " ", width = 4, height = 2,font = ("Montserrat",30),bg="green", relief=tk.RAISED, borderwidth=5)
button1.grid(row = 0, column = 1)
button1.bind("<Button-1>", play)

button1 = tk.Button(frame2, text = " ", width = 4, height = 2,font = ("Montserrat",30),bg="green", relief=tk.RAISED, borderwidth=5)
button1.grid(row = 0, column = 2)
button1.bind("<Button-1>", play)

#2nd row
button1 = tk.Button(frame2, text = " ", width = 4, height = 2,font = ("Montserrat",30),bg="green", relief=tk.RAISED, borderwidth=5)
button1.grid(row = 1, column = 0)
button1.bind("<Button-1>", play)

button1 = tk.Button(frame2, text = " ", width = 4, height = 2,font = ("Montserrat",30),bg="green", relief=tk.RAISED, borderwidth=5)
button1.grid(row = 1, column = 1)
button1.bind("<Button-1>", play)

button1 = tk.Button(frame2, text = " ", width = 4, height = 2,font = ("Montserrat",30),bg="green", relief=tk.RAISED, borderwidth=5)
button1.grid(row = 1, column = 2)
button1.bind("<Button-1>", play)

#3rd row
button1 = tk.Button(frame2, text = " ", width = 4, height = 2,font = ("Montserrat",30),bg="green", relief=tk.RAISED, borderwidth=5)
button1.grid(row = 3, column = 0)
button1.bind("<Button-1>", play)

button1 = tk.Button(frame2, text = " ", width = 4, height = 2,font = ("Montserrat",30),bg="green", relief=tk.RAISED, borderwidth=5)
button1.grid(row = 3, column = 1)
button1.bind("<Button-1>", play)

button1 = tk.Button(frame2, text = " ", width = 4, height = 2,font = ("Montserrat",30),bg="green", relief=tk.RAISED, borderwidth=5)
button1.grid(row = 3, column = 2)
button1.bind("<Button-1>", play)



root.mainloop()