from re import L
from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Label, Style
from string import ascii_uppercase
from functools import partial
import random

guessed_letters = []
let_button = []
GUESSES = 7

def startgame():
    global word
    global hidden_word
    global guessed_letters
    global GUESSES
    GUESSES = 7

    guesses.set("Guesses left: " + str(GUESSES))
    end_message.set("") 
    image_label.set("")
    guessed_letters = [] 
    for x in ascii_uppercase:  
        change_state(x)

    with open("word_list.txt", "r") as file:
        allText = file.read()
        words = list(map(str, allText.split()))
        print(words)
        # get random word from text file
        word = ((random.choice(words)).upper())
        hidden_word = " ".join(word)
        word_label.set(' '.join("_"*len(word)))

def change_state(guess):
    if (let_button[ord(guess) - ord('A')]['state'] == DISABLED):
        let_button[ord(guess) - ord('A')]['state'] = NORMAL

def guess(guess):
    
    global GUESSES
    global guessed_letters

    let_button[ord(guess) - ord('A')]['state'] = DISABLED

    if GUESSES > 0:
        # add guessed letter to list of guessed letters
        guessed_letters.append(guess)
            
        HIDDEN_WORD = list(hidden_word)            
        curr_word = list(word_label.get())

        if guess in word:
            for x in range(len(hidden_word)):
                if (HIDDEN_WORD[x] == guess):
                    curr_word[x] = guess
                word_label.set("".join(curr_word))

        if guess not in word:
            GUESSES -= 1
            guesses.set("Guesses left: " + str(GUESSES))                
            
            if (GUESSES == 6):
                image_label.set("ʕ")
            elif (GUESSES == 5):
                image_label.set("ʕ ·")                
            elif (GUESSES == 4):
                image_label.set("ʕ ·(")
            elif (GUESSES == 3):
                image_label.set("ʕ ·(I")
            elif (GUESSES == 2):
                image_label.set("ʕ ·(I)")
            elif (GUESSES == 1):
                image_label.set("ʕ ·(I)·")
            elif (GUESSES == 0):
                image_label.set("ʕ ·(I)· ʔ")
                end_message.set("You lose! The word was " + word.lower())

        if (curr_word == HIDDEN_WORD):
            end_message.set("You win! :)")

# create the root window
root = Tk()
root.title('Word Game')
root.tk.call('tk', 'scaling', 2.0)
root.state("zoomed")
root.configure(bg='#E6BEFF')

#configure number of columns and rows
root.columnconfigure(9, weight=4)
root.rowconfigure(14, weight=4)
             
# create the title
title = Label(root, text="Word Frenzy", font=('Consolas',25, 'bold', 'underline'))
title.grid(row=0, column=0, rowspan=2, columnspan=9)
title.configure(background='#E6BEFF')

#display current number of guesses
guesses=StringVar()
num_guesses = Label(root, textvariable=guesses, font=('Consolas', 10, 'bold'))
num_guesses.grid(row=0, column=7, columnspan=3, sticky=E, pady=(10,10))
num_guesses.configure(background='#E6BEFF')

#print image for score
image_label=StringVar()
image = Label(root, textvariable=image_label, font=('Consolas', 30, 'bold'))
image.grid(row=2, column=1, columnspan=3, sticky=W)
image.configure(background='#E6BEFF')

#print winning/losing message
end_message=StringVar()
end_game = Label(root, textvariable=end_message, font=('Consolas', 10, 'bold'))
end_game.grid(row=3, column=1, columnspan=3, sticky=W)
end_game.configure(background='#E6BEFF')

#space for word to be displayed
word_label = StringVar()
current_word = Label(root, textvariable= word_label, font = ('Consolas', 30, 'bold'))
current_word.grid(row=2, column=4, columnspan=5, pady=(60,20), padx=(10,10))
current_word.configure(background='#E6BEFF', foreground='#8702C8')

#create the alphabet
num=0
for x in ascii_uppercase:
    to_guess = partial(guess, x)
    button = Button(root, text=x, font=('Consolas', 23, 'bold'), command=to_guess, width=5, state=NORMAL)
    let_button.append(button)
    button.configure(background='#B13AFD')

    if (num <=8):
        button.grid(row=4,column=num%9,pady=20, padx = (3,3), rowspan=2)
    if (num > 8 and num <= 17):
        button.grid(row=6,column=num%9,pady=20, padx = (3,3), rowspan=2)
    if (num > 17 and num <= 26):
        button.grid(row=8,column=num%9,pady=20, padx = (3,3), rowspan=2)
    num+=1

# reset button
reset = Button(root, text="Restart", command=startgame, font=("Consolas",15, 'bold'))
reset.grid(row=8, column=8, pady=20, rowspan=2)
reset.configure(background='#B13AFD')
                     
# Run the application
if __name__ == "__main__":
    startgame()
    root.mainloop()