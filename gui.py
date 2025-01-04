import tkinter as tk
import random

def roll_dice():
    """Rolls the dice and updates the result label."""
    dice_result = random.randint(1, 6)
    result_label.config(text=f"You rolled: {dice_result}")
=
root = tk.Tk()
root.title("Dice Game")
root.geometry("300x200")
root.resizable(False, False)


title_label = tk.Label(root, text="Dice Game", font=("Helvetica", 18, "bold"))
title_label.pack(pady=10)

roll_button = tk.Button(root, text="Roll Dice", font=("Helvetica", 14), command=roll_dice)
roll_button.pack(pady=20)

result_label = tk.Label(root, text="", font=("Helvetica", 14))
result_label.pack(pady=10)

root.mainloop()
