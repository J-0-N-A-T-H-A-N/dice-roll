from random import randint
from tkinter import *

def roll_dice():
    num_of_dice = int(spin_num_of_dice.get())
    num_of_sides = int(spin_num_of_sides.get())
    spin_num_of_dice.config(state="disabled")
    spin_num_of_sides.config(state="disabled")
    count = 1
    while count <= num_of_dice:
        roll = randint(1, num_of_sides)
        label_dice = Label(text=roll,
                            width=7,
                            height=4,
                            font=("Arial", 12),
                            borderwidth=1,
                            border=1,
                            relief="solid",
                            padx=20,
                            pady=20)
        label_dice.grid(column=count, row=1, padx=5)
        count += 1


window = Tk()
window.config(pady=20, padx=20)
window.title("Dice Roll")


label_num_of_dice = Label(text="Number of dice: ", font=("Arial", 10))
label_num_of_dice.grid(column=1, row=2, columnspan=3)
spin_num_of_dice = Spinbox(wrap=True, from_=1, to=6, width=5)
spin_num_of_dice.grid(column=4, row=2, pady=10)

label_num_of_sides = Label(text="Number of sides: ", font=("Arial", 10))
label_num_of_sides.grid(column=1, row=3, columnspan=3)

spin_num_of_sides = Spinbox(wrap=True, values=("6", "8", "10", "12", "20"), width=5)
spin_num_of_sides.grid(column=4, row=3, pady=10)

button_draw = Button(text="R O L L", command=roll_dice, font=("Arial", 16))
button_draw.grid(row=2, column=5, padx=20, columnspan=2, rowspan=2)

window.mainloop()
