from tkinter import *
from random import choice
import pandas

BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
to_learn = {}

# -----------------------------data setup-------------------------------#


try:
    data = pandas.read_csv('data/words_to_learn.csv')
except FileNotFoundError:
    original_data = pandas.read_csv('data/french_words.csv')
    to_learn = original_data.to_dict(orient='records')
else:
    to_learn = data.to_dict(orient='records')


# ----------------------------card logic------------------------------- #


def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = choice(to_learn)
    canvas.itemconfig(the_word, text=current_card['French'], fill='black')
    canvas.itemconfig(title, text='French', fill='black')
    canvas.itemconfig(flash_card, image=flashcard_image)
    flip_timer = window.after(3000, func=flip_card)


def flip_card():
    canvas.itemconfig(the_word, text=current_card['English'], fill='white')
    canvas.itemconfig(title, text='English', fill='white')
    canvas.itemconfig(flash_card, image=flashcard_image_back)


def is_known():
    to_learn.remove(current_card)
    data = pandas.DataFrame(to_learn)
    data.to_csv('data/words_to_learn.csv', index=False)
    next_card()


# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title('Flashy')
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_card)

# Canvas setup
canvas = Canvas(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)
flashcard_image = PhotoImage(file='images/card_front.png')
flashcard_image_back = PhotoImage(file='images/card_back.png')
flash_card = canvas.create_image(400, 260, image=flashcard_image)
title = canvas.create_text(400, 150, text='', font=('Ariel', 40, 'italic'))
the_word = canvas.create_text(400, 263, text='', font=('Ariel', 60, 'bold'))
canvas.grid(row=0, column=0, columnspan=2)

# button setup
correct_image = PhotoImage(file='images/right.png')
correct_button = Button(image=correct_image, highlightthickness=0, command=is_known)
correct_button.grid(row=1, column=0)

wrong_image = PhotoImage(file='images/wrong.png')
wrong_button = Button(image=wrong_image, highlightthickness=0, command=next_card)
wrong_button.grid(row=1, column=1)

next_card()

window.mainloop()
