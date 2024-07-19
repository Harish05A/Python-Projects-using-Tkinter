from tkinter import *
import random
from PIL import Image, ImageTk

# Initialize the main window
root = Tk()
root.geometry("500x600")
root.title("Rock Paper Scissors Game")
root.config(bg="#222222")
# Dictionary to map numbers to choices
computer_value = {"0": "Rock", "1": "Paper", "2": "Scissors"}

# Function to reset the game
def reset_game():
    b1["state"] = "active"
    b2["state"] = "active"
    b3["state"] = "active"
    l1.config(text="Player")
    l3.config(text="Computer")
    l4.config(text="")

# Function to disable buttons after a choice is made
def button_disable():
    b1["state"] = "disable"
    b2["state"] = "disable"
    b3["state"] = "disable"
    

# Function for Rock choice
def isrock():
    c_v = computer_value[str(random.randint(0, 2))]
    Player_image.config(file="Rock.png")
    if c_v == "Rock":
        match_result = "Match Draw"
        Comp_image.config(file="Rock.png")
    elif c_v == "Scissors":
        match_result = "Player Wins"
        Comp_image.config(file="Scissor.png")
    else:
        match_result = "Computer Wins"
        Comp_image.config(file="Paper.png")
    l4.config(text=match_result)
    l1.config(text="Rock")
    l3.config(text=c_v)
    button_disable()

# Function for Paper choice
def ispaper():
    c_v = computer_value[str(random.randint(0, 2))]
    Player_image.config(file="Paper.png")
    if c_v == "Paper":
        Comp_image.config(file="Paper.png")
        match_result = "Match Draw"
    elif c_v == "Rock":
        Comp_image.config(file="Rock.png")
        match_result = "Player Wins"
    else:
        Comp_image.config(file="Scissor.png")
        match_result = "Computer Wins"
    l4.config(text=match_result)
    l1.config(text="Paper")
    l3.config(text=c_v)
    button_disable()

# Function for Scissors choice
def isscissors():
    c_v = computer_value[str(random.randint(0, 2))]
    Player_image.config(file="Scissor.png")
    if c_v == "Scissors":
        Comp_image.config(file="Scissor.png")
        match_result = "Match Draw"
    elif c_v == "Paper":
        Comp_image.config(file="Paper.png")
        match_result = "Player Wins"
    else:
        Comp_image.config(file="Rock.png")
        match_result = "Computer Wins"
    l4.config(text=match_result)
    l1.config(text="Scissors")
    l3.config(text=c_v)
    button_disable()

# GUI Layout
Label(root, text="Rock Paper Scissors", font="Poppins 25 bold", bg="#222222",fg="#CD9C20").pack(pady=20)

frame = Frame(root,bg="#222222")
frame.pack()

l1 = Label(frame, text="Player", font="Poppins 15 bold", bg="#222222",fg="#CD9C20")
l2 = Label(frame, text="VS", font="Poppins 17 bold", bg="#222222",fg="#CD9C20")
l3 = Label(frame, text="Computer", font="Poppins 15 bold", bg="#222222",fg="#CD9C20")

l1.pack(side=LEFT)
l2.pack(side=LEFT)
l3.pack(side=LEFT)

Player_image = PhotoImage(file="Rock.png")
Comp_image = PhotoImage(file="Scissor.png")
# Create a label to display the image
Player_image_label = Label(root, image=Player_image,borderwidth=0, bg="#222222")
Comp_image_label = Label(root, image=Comp_image,borderwidth=0, bg="#222222")

Player_image_label.pack(padx=10,pady=20)
Comp_image_label.pack(padx=30,pady=20)

l4 = Label(root, text="", font="Poppins 20 bold", bg="#F2ECDD", width=15, borderwidth=2, relief="solid")
l4.pack(pady=35)

frame1 = Frame(root,bg="#222222")
frame1.pack()

b1 = Button(frame1, text="Rock", font="Poppins 10 bold", width=7, command=isrock, bg="#F5CB5C")
b2 = Button(frame1, text="Paper", font="Poppins 10 bold", width=7, command=ispaper, bg="#F5CB5C")
b3 = Button(frame1, text="Scissors", font="Poppins 10 bold", width=7, command=isscissors, bg="#F5CB5C")

b1.pack(side=LEFT, padx=10)
b2.pack(side=LEFT, padx=10)
b3.pack(side=LEFT, padx=10)

Button(root, text="Reset", font=10,bg="#4A0754", fg="white", command=reset_game).pack(pady=20)

# Run the main loop
root.mainloop()
