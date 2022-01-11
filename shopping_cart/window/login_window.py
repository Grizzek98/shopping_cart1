from tkinter import *
import tkinter

class LoginWindow():

    def __init__(self, window):
        # initialize login window
        self.window = window
        self.username_get = StringVar()
        self.password_get = StringVar()

    def window_start(self):
        self.window.rowconfigure(0, weight=1)
        self.window.columnconfigure(0, weight=1)
        self.welcome_frame = tkinter.Frame(self.window, bg='blue')
        self.welcome_frame.grid(row=0, column=0, sticky='nsew')
        self.create_widgets()

    def create_widgets(self):
        # create widget objects
        username_label = Label(self.window, text = "Username:", font = ("Times New Roman", 12, "bold"))
        password_label = Label(self.window, text = "Password:", font = ("Times New Roman", 12, "bold"))
        username_entry = Entry(self.window, textvariable = self.username_get, font = ("Times New Roman", 12))
        password_entry = Entry(self.window, textvariable = self.password_get, font = ("Times New Roman", 12), show = "*")
        submit_button = Button(self.window, text = "Submit", command = self.submit_btn_click)

        # widget placement in grid style
        username_label.grid(row = 0, column = 0)
        password_label.grid(row = 1, column = 0)
        username_entry.grid(row = 0, column = 1)
        password_entry.grid(row = 1, column = 1)
        submit_button.grid(row = 2, column = 1)

    def submit_btn_click(self):
        # executed on submit button clicked
        username = self.username_get.get()
        password = self.password_get.get()

        print("username: ", username)
        print("Password: ", password)

        # clear the variables
        self.username_get.set("")
        self.password_get.set("")