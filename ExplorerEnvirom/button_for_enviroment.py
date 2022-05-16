from tkinter import Button, Entry


class Buttons:


    def button_open(self, open):
        button_copy = Button(self, text='Open', bg='red', font=40, command=open)
        button_copy.grid(column=1, row=0)

    def button_back(self, back):
        button_move = Button(self, text='Back', bg='red', font=40, command=back)
        button_move.grid(column=2, row=0)

    def button_create(self, copy):
        button_move = Button(self, text='CreateFolder', bg='red', font=40, command=copy)
        button_move.grid(column=3, row=0)

    def enter_and_label(self):
        entry = Entry(self, fg="yellow", bg="blue", width=60)
        entry.insert(0, "Enter absolute path for create folder and then click on the button")
        entry.grid(column=4, row=0)



