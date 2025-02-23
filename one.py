from tkinter import *

class Calculator:
    def __init__(self, master):
        master.title("Calculator")
        master.geometry("342x520+0+0")
        master.resizable(False, True)
        master.configure(background="gray")

        self.equation = StringVar()
        self.entry_value = ''
        Entry(master, width=17, background='#fff', font=('Arial Bold', 28), textvariable=self.equation).place(x=0, y=0)

        # Row 1
        Button(master, width=11, height=4, text='(', relief='flat', background="white",
               command=lambda: self.show('(')).place(x=0, y=100)
        Button(master, width=11, height=4, text=')', relief='flat', background="white",
               command=lambda: self.show(')')).place(x=90, y=100)
        Button(master, width=11, height=4, text='%', relief='flat', background="white",
               command=lambda: self.show('%')).place(x=180, y=100)
        Button(master, width=11, height=4, text='C', relief='flat', background="white",
               command=self.clear).place(x=270, y=100)

        # Row 2
        Button(master, width=11, height=4, text='7', relief='flat', background="white",
               command=lambda: self.show(7)).place(x=0, y=170)
        Button(master, width=11, height=4, text='8', relief='flat', background="white",
               command=lambda: self.show(8)).place(x=90, y=170)
        Button(master, width=11, height=4, text='9', relief='flat', background="white",
               command=lambda: self.show(9)).place(x=180, y=170)
        Button(master, width=11, height=4, text='/', relief='flat', background="white",
               command=lambda: self.show('/')).place(x=270, y=170)

        # Row 3
        Button(master, width=11, height=4, text='4', relief='flat', background="white",
               command=lambda: self.show(4)).place(x=0, y=240)
        Button(master, width=11, height=4, text='5', relief='flat', background="white",
               command=lambda: self.show(5)).place(x=90, y=240)
        Button(master, width=11, height=4, text='6', relief='flat', background="white",
               command=lambda: self.show(6)).place(x=180, y=240)
        Button(master, width=11, height=4, text='X', relief='flat', background="white",
               command=lambda: self.show('*')).place(x=270, y=240)

        # Row 4
        Button(master, width=11, height=4, text='1', relief='flat', background="white",
               command=lambda: self.show(1)).place(x=0, y=310)
        Button(master, width=11, height=4, text='2', relief='flat', background="white",
               command=lambda: self.show(2)).place(x=90, y=310)
        Button(master, width=11, height=4, text='3', relief='flat', background="white",
               command=lambda: self.show(3)).place(x=180, y=310)
        Button(master, width=11, height=4, text='-', relief='flat', background="white",
               command=lambda: self.show('-')).place(x=270, y=310)

        # Row 5
        Button(master, width=11, height=4, text='0', relief='flat', background="white",
               command=lambda: self.show(0)).place(x=0, y=380)
        Button(master, width=11, height=4, text='.', relief='flat', background="white",
               command=lambda: self.show('.')).place(x=90, y=380)
        Button(master, width=11, height=4, text='=', relief='flat', background="white",
               command=self.solve).place(x=180, y=380)
        Button(master, width=11, height=4, text='+', relief='flat', background="white",
               command=lambda: self.show('+')).place(x=270, y=380)

    def show(self, value):
        self.entry_value += str(value)
        self.equation.set(self.entry_value)

    def clear(self):
        self.entry_value = ''
        self.equation.set(self.entry_value)

    def solve(self):
        result = eval(self.entry_value)
        self.equation.set(result)

root = Tk()
calculator = Calculator(root)
root.mainloop()