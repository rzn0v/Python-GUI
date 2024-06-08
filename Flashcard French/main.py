BACKGROUND_COLOR = "#B1DDC6"

from tkinter import *
import pandas as pd
import random
from tkinter import messagebox
random_choice = {}
to_learn = {}

try:
    data = pd.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    new_data = pd.read_csv("data/french_words.csv")
    to_learn = new_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")


def english_word():
    global random_choice
    english = random_choice["English"]
    canvas.itemconfig(card_image, image=card_back)
    canvas.itemconfig(card_word, text=english, fill="white")
    canvas.itemconfig(card_title, text="English", fill="white")

def new_word():
    global random_choice, flip_timer
    window.after_cancel(flip_timer)
    random_choice = random.choice(to_learn)
    french = random_choice["French"]
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=french, fill="black")
    canvas.itemconfig(card_image, image=card_front)
    flip_timer = window.after(3000, english_word)

def is_known():
    if len(to_learn) == 0:
        messagebox.showinfo(title="Yay!", message="You learnt all the words")
    else:
        to_learn.remove(random_choice)
        data = pd.DataFrame(to_learn)
        data.to_csv("data/words_to_learn.csv", index=False)
        new_word()
    
    

window = Tk()
window.title("Flashy")
window.config(bg=BACKGROUND_COLOR, padx=40, pady=40)
flip_timer = window.after(3000, english_word)

canvas = Canvas(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)
card_front = PhotoImage(file="images/card_front.png")
card_back = PhotoImage(file="images/card_back.png")
card_image = canvas.create_image(400, 263, image=card_front)
card_title = canvas.create_text(400, 150, text="", font=("Arial", 22, "italic"))
card_word = canvas.create_text(400, 263, text="", font=("Arial", 35, "bold"))
canvas.grid(column=0, row=0, columnspan=2)

known_img = PhotoImage(file="images/right.png")
unknown_img = PhotoImage(file="images/wrong.png")
known = Button(image=known_img, highlightthickness=0, command=is_known)
unknown = Button(image=unknown_img, highlightthickness=0, command=new_word)

known.grid(column=0, row=1)
unknown.grid(column=1, row=1)

new_word()

window.mainloop()