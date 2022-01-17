from tkinter import *
import tkinter
import json


class WindowHandler(tkinter.Tk):

    def __init__(self):
        tkinter.Tk.__init__(self)
        self._frame = None
        self.title("Tkinter Program")
        self.geometry("500x500")
        self.switch_frame(WelcomeWindow)

    def switch_frame(self, frame_class):
        new_frame = frame_class(self)
        if self._frame is not None:
            self._frame.destroy()
        self._frame = new_frame
        self._frame.pack()


class WelcomeWindow(tkinter.Frame):

    def __init__(self, root):
        tkinter.Frame.__init__(self, root)

        welcome_label = Label(self, text="Tkinter Program", font=("Times New Roman", 20, "bold"))
        continue_btn = Button(self, text="Continue", command=lambda: root.switch_frame(LoginWindow))

        welcome_label.pack()
        continue_btn.pack()


class LoginWindow(tkinter.Frame):

    def __init__(self, root):
        tkinter.Frame.__init__(self, root)
        
        self.username_get = StringVar()
        self.password_get = StringVar()

        username_label = Label(self, text = "Username:", font = ("Times New Roman", 12, "bold"))
        password_label = Label(self, text = "Password:", font = ("Times New Roman", 12, "bold"))
        username_entry = Entry(self, textvariable = self.username_get, font = ("Times New Roman", 12))
        password_entry = Entry(self, textvariable = self.password_get, font = ("Times New Roman", 12), show = "*")
        submit_button = Button(self, text = "Submit", command = self.submit_btn_click)

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

        login_file = open('C:\\python\\My Python\\shopping_cart1\\shopping_cart\\window\\user_data\\' + 'login_info.json')
        data = json.load(login_file)
        for user in data:
            if username == data[user].get('username') and password == data[user].get('password'):
                print('yay!')

        print("Username: ", username)
        print("Password: ", password)

        # clear the variables
        self.username_get.set("")
        self.password_get.set("")