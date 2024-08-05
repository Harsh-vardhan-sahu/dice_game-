import tkinter as tk
import random

def enter_game():
    enter_frame.pack_forget()
    game_frame.pack()

def roll_dice():
    dice = ['\u2680', '\u2681', '\u2682', '\u2683', '\u2684', '\u2685']
    label.configure(text=f'{random.choice(dice)}', padx=22, pady=22, anchor='nw', bg="white", fg="red")
    window.geometry("400x340")

window = tk.Tk()
window.title("Dice Game")
window.geometry("660x460")

enter_frame = tk.Frame(window, relief="sunken")
enter_frame.pack(pady=0, side='left', anchor='n')

label = tk.Label(window, text="", font=('Helvetica', 170))
label.pack()

enter_button = tk.Button(enter_frame, text="Enter Game", fg="blue", borderwidth=4, command=enter_game,)

enter_button.pack(pady=10, padx=20, side='right')

game_frame = tk.Frame(window, relief='sunken')

roll_button = tk.Button(game_frame, text="Roll Dice", fg='red', command=roll_dice)
roll_button.pack(pady=10)

photo = tk.PhotoImage(file="d1.png")
har_label = tk.Label(enter_frame, image=photo)
har_label.pack()

a = tk.Label(enter_frame, text="Dice Game", bg='blue', fg='white', font=("Comic Sans MS", 14))
a.pack(side='top', fill='x')

a = tk.Label(enter_frame, text="by:-Harsh Vardhan Sahu (0901A1221029)", fg='white',bg='black', font=("Comic Sans MS", 10))
a.pack(anchor='se', side='left')

result_label = tk.Label(game_frame, text="")
result_label.pack()

game_frame.pack_forget()

window.mainloop()
