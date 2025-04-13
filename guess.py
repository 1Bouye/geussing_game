# Importing the tkinter module for GUI (Graphical User Interface)
import tkinter as tk
from tkinter import *

# Importing the random module to generate random numbers
import random

# Creating the main application window
win = tk.Tk()

# Setting the size of the window to 750x750 pixels
win.geometry("750x750")

# Setting the title of the window
win.title("BouyeCode")

# Creating variables to store hint message, score, final score, and the user's guess
hint = StringVar()         # This will show messages like "Guess too high" or "You won"
score = IntVar()           # This is the current score (chances left)
final_score = IntVar()     # This will update and display the score to the user
guess = IntVar()           # This holds the number the user enters

# Generating a random number between 1 and 50 that the user has to guess
num = random.randint(1, 50)

# Setting the first message to be shown
hint.set("Guess a number between 1 to 50 ")

# Giving the player 5 chances to guess
score.set(5)

# Setting final_score equal to the current score at the start
final_score.set(score.get())

# This is the main function that runs every time the user makes a guess
def fun():
    # Get the number the user entered
    x = guess.get()

    # Update the final score
    final_score.set(score.get())

    # Check if the user still has chances left
    if score.get() > 0:

        # If the number is outside the guessing range (0 to 20), show warning and reduce 1 chance
        if x > 20 or x < 0:
            hint.set("You just lost 1 Chance")
            score.set(score.get() - 1)
            final_score.set(score.get())

        # If the user's guess is correct
        elif num == x:
            hint.set("Congratulation YOU WON!!!")
            score.set(score.get() - 1)
            final_score.set(score.get())

        # If the guess is too low
        elif num > x:
            hint.set("Your guess was too low: Guess a number higher ")
            score.set(score.get() - 1)
            final_score.set(score.get())

        # If the guess is too high
        elif num < x:
            hint.set("Your guess was too High: Guess a number Lower ")
            score.set(score.get() - 1)
            final_score.set(score.get())

    # If no chances are left, show Game Over message
    else:
        hint.set("Game Over You Lost")

# Creating an input field where the user will type their guess
# - `textvariable=guess` links the input to our guess variable
# - `width=3` means only 3 characters wide
# - `font=('Ubuntu', 50)` makes the input big and visible
# - `relief=GROOVE` adds a groove border style
# - `place` positions it in the middle of the window
Entry(win, textvariable=guess, width=3, font=('Ubuntu', 50), relief=GROOVE).place(relx=0.5, rely=0.3, anchor=CENTER)
