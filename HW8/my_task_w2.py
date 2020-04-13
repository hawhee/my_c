import tkinter
import os.path
import json

filename = 'my_tasks.json'

def read(filename):
    with open(filename) as file:
        global load
        load = json.load(file)

if os.path.isfile(filename):
    read(filename)
else:
    load = []

def one():
    new_task = {'Задача:': task.get(), 'Категория:': category.get(), 'Время:': time.get()}
    load.append(new_task)
    task.delete(0, 'end')
    category.delete(0, 'end')
    time.delete(0, 'end')

def two():
    if load:
        text.delete(1.0, 'end')
        for element in load:
            print(element.items())
            for key, value in element.items():
                text.insert('end', key + ' ' + value + '; ')
            text.insert('end', '\n\n')
    else:
        text.insert('end', 'Вы еще не добавили ни одной задачи.')

def three():
    with open(filename, 'w') as w_file:
        json.dump(load, w_file)
        window.destroy()

def center(e):
    w = int(root.winfo_width() / 3.5)
    s = 'Менеджер задач'.rjust(w//2)
    root.title(s)

root = tkinter.Tk()
root.bind("<Configure>", center)

task_text = tkinter.Label(root, text = 'Задача:')
task_text.grid(row = 0, column = 0, sticky = 'N', padx=5)

task = tkinter.Entry(root)
task.grid(row = 0, column = 1, sticky = 'N', padx=5)

category_text = tkinter.Label(root, text = 'Категория:')
category_text.grid(row = 1, column = 0, sticky = 'N', padx=5)

category = tkinter.Entry(root)
category.grid(row = 1, column = 1, sticky = 'N', padx=5)

time_text = tkinter.Label(root, text = 'Время:')
time_text.grid(row = 2, column = 0, sticky = 'N', padx=5)

time = tkinter.Entry(root)
time.grid(row = 2, column = 1, sticky = 'N', padx=5)

text = tkinter.Text(width=25, height = 10)
text.grid(row = 0, column = 3, rowspan = 10, padx=5)

add_task = tkinter.Button(root, text = 'Добавить задачу', command = one)
add_task.grid(row = 3, column = 1)

list_of_tasks = tkinter.Button(root, text = 'Список задач', command = two)
list_of_tasks.grid(row = 4, column = 1)

exit = tkinter.Button(root, text = 'Выход', command = three)
exit.grid(row = 5, column = 1)

root.mainloop()
