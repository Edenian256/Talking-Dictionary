from tkinter import *
import json
from difflib import get_close_matches
from tkinter import messagebox
import pyttsx3

engine = pyttsx3.init()
voice = engine.getProperty('voices')
# setting a male voice
engine.setProperty('voice', voice[0].id)


def search():
    data = json.load(open('data.json'))
    word = word_entry_field_label.get()
    word = word.lower()
    if word in data:
        meaning = data[word]
        print(meaning)
        text_area.delete(1.0, END)
        for item in meaning:
            text_area.insert(END, u'\u2022' + item + '\n\n')
    elif len(get_close_matches(word, data.keys())) > 0:
        close_match = get_close_matches(word, data.keys())[0]
        res = messagebox.askyesno("confirm", f' Did you mean "{close_match}" instead?')
        if res:
            word_entry_field_label.delete(0, END)
            word_entry_field_label.insert(END, close_match)
            meaning = data[close_match]
            text_area.delete(1.0, END)
            for item in meaning:
                text_area.insert(END, u'\u2022' + item + '\n\n')
        else:
            messagebox.showerror('error', f'"{word}" could not found')
            word_entry_field_label.delete(0, END)
            text_area.delete(1.0, END)
    else:
        messagebox.showinfo('Information', f'"{word}" could not found')
        word_entry_field_label.delete(0, END)
        text_area.delete(1.0, END)


def clear():
    word_entry_field_label.delete(0, END)
    text_area.delete(1.0, END)


def iexit():
    res = messagebox.askyesno('confirm', 'Do you want to exit? ')
    if res:
        root.destroy()
    else:
        pass


def word_audio():
    engine.say(word_entry_field_label.get())
    engine.runAndWait()


def meaning_audio():
    engine.say(text_area.get(1.0, END))
    engine.runAndWait()


# GUI PART

root = Tk()

root.title("Talking Dictionary created by Abenezer Asamenew")

# width and height of the entire window
root.geometry('1000x626+100+30')
root.resizable(False, False)

bgimage = PhotoImage(file='bg.png')
bgLabel = Label(root, image=bgimage)
bgLabel.place(x=0, y=0)
# root.config(bg="snow")

enter_word = Label(root, text='Enter word', font=('castellar', 29, 'bold'), foreground='grey4', background='whitesmoke')
enter_word.place(x=530, y=20)

word_entry_field_label = Entry(root, font=('arial', 23, 'bold'), justify=CENTER, bd=4, relief=GROOVE)
word_entry_field_label.place(x=510, y=80)

search_image = PhotoImage(file='search1.png')
search_button = Button(root, image=search_image, bd=0, bg='whitesmoke', cursor='hand2', activebackground='whitesmoke',
                       command=search)
search_button.place(x=620, y=150)

mic_image = PhotoImage(file='mic.png')
mic_button = Button(root, image=mic_image, bd=0, bg='whitesmoke', cursor='hand2', activebackground='whitesmoke',
                    command=word_audio)
mic_button.place(x=710, y=153)

meaning_label = Label(root, text='Meaning', font=('castellar', 29, 'bold'), foreground='grey4', background='whitesmoke')
meaning_label.place(x=580, y=240)

text_area = Text(root, width=39, height=8, font=('arial', 18, 'bold'), bd=4, relief=GROOVE)
text_area.place(x=460, y=300)

audio_image = PhotoImage(file='microphone.png')
audio_button = Button(root, image=audio_image, bd=0, bg='whitesmoke', cursor='hand2', activebackground='whitesmoke',
                      command=meaning_audio)
audio_button.place(x=530, y=555)

clear_image = PhotoImage(file='clear.png')
clear_button = Button(root, image=clear_image, bd=0, bg='whitesmoke', cursor='hand2', activebackground='whitesmoke',
                      command=clear)
clear_button.place(x=660, y=555)

exit_image = PhotoImage(file='exit.png')
exit_button = Button(root, image=exit_image, bd=0, bg='whitesmoke', cursor='hand2', activebackground='whitesmoke',
                     command=iexit)
exit_button.place(x=790, y=555)


def enter_function(event):
    search_button.invoke()


root.bind('<Return>', enter_function)

# keeps the window open
root.mainloop()
