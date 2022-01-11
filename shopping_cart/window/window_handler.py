from tkinter import *
import tkinter
from window.login_window import LoginWindow
from window.welcome_window import WelcomeWindow


class WindowHandler:

    def __init__(self):

        # initialize window settings
        self.root = Tk()
        self.root.title("tkinter program")
        self.root.geometry("200x200")

        self.welcome_window = WelcomeWindow(self.root)
        self.login_window = LoginWindow(self.root)

        # instantiate frames
        self.welcome_window_frame = tkinter.Frame(self.root)
        self.login_window_frame = tkinter.Frame(self.root)
        self.other_frame = tkinter.Frame(self.root)

        self.program_start()

    def program_start(self):
        self.create_frames()
        self.welcome_window.window_start(self.welcome_window_frame)
        # self.login_window.window_start()
        self.show_frame(self.welcome_window_frame)
        self.root.mainloop()

    def create_frames(self):
        for frame in (self.welcome_window_frame, self.login_window_frame):
            frame.grid(row=0, column=0, sticky='nsew')

    def show_frame(self, frame):
        frame.tkraise()