from tkinter import Tk, END, Listbox, Entry, SINGLE
import os
import shutil
from ExplorerEnvirom.button_for_enviroment import Buttons
from ExplorerEnvirom.frame_button import DifferenceFrame

place = "C:\\"
place_list = ['c:\\']


class Enviroment:
    '''
    Все окружение которое используется
    '''
    windows_explorer = Tk()
    windows_explorer.title('Explorer')
    windows_explorer.geometry('700x550')

    frame_for_all_button = DifferenceFrame.frame_for_button(windows_explorer)
    frame_for_listbox = DifferenceFrame.frame_for_library(windows_explorer)


os.chdir(place)
place_with_data = os.listdir()
listbox_for_library = Listbox(Enviroment.frame_for_listbox, selectmode=SINGLE)
listbox_for_library.place(x=0, y=42, relwidth=1, relheight=1)
for i in place_with_data:
    listbox_for_library.insert(END, i)

entry = Entry(Enviroment.frame_for_all_button, fg="yellow", bg="blue", width=60)
entry.insert(0, "Enter absolute path for create folder and then click on the button")
entry.grid(column=4, row=0)


def do_under_button_open():
    '''
     Действия над кнопкой открыть,
     перемещение по папкам
    '''
    global place_with_data, place_list
    index = listbox_for_library.curselection()[0]
    name = place_with_data[index]
    path = place_list[-1]
    newPath = path + '\\' + name
    os.chdir(newPath)
    place_list.append(newPath)
    place_with_data.clear()
    place_with_data = os.listdir()
    size = listbox_for_library.size()
    listbox_for_library.delete(0, size)
    for i in place_with_data:
        listbox_for_library.insert(END, i)


def do_under_button_back():
    '''
     Действия над кнопкой назад.
     перемещение по папкам
    '''
    global place_with_data, place_list
    if len(place_list) == 1:
        newPath = place_list[-1]
    else:
        newPath = place_list.pop()
        newPath = place_list[-1]
    os.chdir(newPath)
    place_with_data.clear()
    place_with_data = os.listdir()
    size = listbox_for_library.size()
    listbox_for_library.delete(0, size)
    for i in place_with_data:
        listbox_for_library.insert(END, i)


def do_under_button_create_folder():

    '''
     Создаем папку и пишем путь
    '''
    name = entry.get()
    os.makedirs(name)

Buttons.button_back(Enviroment.frame_for_all_button, do_under_button_back)
Buttons.button_open(Enviroment.frame_for_all_button, do_under_button_open)
Buttons.button_create(Enviroment.frame_for_all_button, do_under_button_create_folder)



Enviroment.windows_explorer.mainloop()

