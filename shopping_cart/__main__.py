from tkinter import *
from tkinter.ttk import *


def main():
    root = Tk()
    root.title("First Tkinter Program")

    frame = Frame(root)
    frame.pack()

    button = Button(frame, text = "Bro")
    button.pack()

    root.mainloop()

if __name__ == "__main__":
    main()