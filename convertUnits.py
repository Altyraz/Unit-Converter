from tkinter import *
from tkinter import ttk
import math
import sys


class ConvertUnits:
    def __init__(self) -> None:
        self.root = Tk()
        self.root.configure(background='white')
        self.root.title("Unit Converter")
        self.root.geometry("800x550")


        self.lblHeader = Label(self.root, text="Choose the units from and to which you want to convert", bg=
                               "white", fg="dark grey", font=("Arial", 18))
        self.lblHeader.grid(row=1, column=1, padx=80, pady=10)
        self.lblinitialUnit = Label(self.root, text="Which unit do you want to convert from?", bg="white", fg="black", font=
                                    ("Arial", 14))
        self.lblinitialUnit.grid(row=2, column=1, padx=100, pady=10)


        self.root.mainloop()