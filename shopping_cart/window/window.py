from tkinter import *
from tkinter.ttk import *

class window():

    def __init__(self):
        self.window = Tk()
        self.window.geometry("600x800")
        self.window.title("Tkinter Program")

        # username and password variable creation
        username_get = StringVar()
        password_get = StringVar()

        # submit button logic
        def submit():
            # get the values currently held in the boxes
            username = username_get.get()
            password = password_get.get()

            print("username: ", username)
            print("Password: ", password)

            # clear the variables
            username_get.set("")
            password_get.set("")

        # widget creation
        username_label = Label(self.window, text = "Username:", font = ("Times New Roman", 12, "bold"))
        password_label = Label(self.window, text = "Password:", font = ("Times New Roman", 12, "bold"))
        username_entry = Entry(self.window, textvariable = username_get, font = ("Times New Roman", 12))
        password_entry = Entry(self.window, textvariable = password_get, font = ("Times New Roman", 12), show = "*")
        submit_button = Button(self.window, text = "Submit", command = submit)

        # widget placement in grid style
        username_label.grid(row = 0, column = 0)
        password_label.grid(row = 1, column = 0)
        username_entry.grid(row = 0, column = 1)
        password_entry.grid(row = 1, column = 1)
        submit_button.grid(row = 2, column = 1)

        self.window.mainloop()