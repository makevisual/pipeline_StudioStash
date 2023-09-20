import tkinter as tk
from tkinter import ttk
from sdst_classes import *

class SDSTMainUi:
    def __init__(self, root):
        self.root = root
        self.root.title("Python UI Example")

        self.label = tk.Label(root, text="Welcome to My UI")
        self.label.pack(pady=10)

        self.button1 = tk.Button(root, text="Show Message", command=self.show_message)
        self.button1.pack()

        self.button2 = tk.Button(root, text="Exit", command=self.exit_app)
        self.button2.pack(pady=10)

    def show_message(self):
        messagebox.showinfo("Message", "Hello, this is a message!")

    def exit_app(self):
        self.root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    sdstMainUi = SDSTMainUi(root)
    root.mainloop()
