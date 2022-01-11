from tkinter import *
import tkinter

class WelcomeWindow:
    def __init__(self, window):
        self.window = window

    def window_start(self, welcome_window_frame):
        self.welcome_window_frame = welcome_window_frame
        self.create_widgets()
    
    def create_widgets(self):
        # create widget objects
        label1 = Label(self.welcome_window_frame, text="tkinter program!", font=("Times New Roman", 20, "bold"))
        continue_btn = Button(self.welcome_window_frame, text="Continue", command=self.continue_btn_click)

        # place widgets on screen
        label1.pack()
        continue_btn.pack()

    def continue_btn_click(self):
        return