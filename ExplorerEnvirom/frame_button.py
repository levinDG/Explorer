from tkinter import Frame

class DifferenceFrame:

    def frame_for_button(self):
        frame_for_button = Frame(self, bg='yellow')
        frame_for_button.place(relx=0, rely=0, relwidth=1, relheight=0.09)
        return

    def frame_for_library(self):
        frame_for_library = Frame(self)
        frame_for_library.place(relx=0, rely=0.09, relwidth=1, relheight=1)


