import tkinter
import random

dictionary = {'chicken':'курица','python':'питон','snake':'змея'}
window = tkinter.Tk()
label = tkinter.Label(window, text = 'Случайное слово:').pack()
word = tkinter.StringVar()
word.set(random.choice(list(dictionary.keys())))
label = tkinter.Label(window, text = word.get()).pack()
label = tkinter.Label(window, text = 'Укажите перевод слова:').pack()
entry = tkinter.Entry(window)
entry.pack()
label = tkinter.Label(window)
label.pack()

def click():
    entry_word = tkinter.StringVar()
    entry_word = entry.get()
    if entry_word == dictionary.get(word.get()):
        label.config(text = 'Угадали')
    else:
        label.config(text = 'Не угадали')

button = tkinter.Button(window, text = 'Проверить',command = click)
button.pack()

exit = tkinter.Button(window, text = 'Выход', command = window.destroy)
exit.pack()

window.mainloop()
