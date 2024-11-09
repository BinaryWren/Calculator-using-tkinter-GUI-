from tkinter import Tk, Entry, Button, StringVar


class Calculator:
    def __init__(self, master):
        master.title("Calculator")
        master.geometry('350x420+0+0')
        master.config(bg='gray')
        master.resizable(False, False)

        self.equation = StringVar()
        self.entry_value = ''

        Entry(master, width=17, bg='#fff', font=('Arial Bold', 28), textvariable=self.equation).grid(row=0, column=0,
                                                                                                     columnspan=4)

        Button(master, width=11, height=4, text='(', relief='flat', bg='white', command=lambda: self.show('(')).grid(
            row=1, column=0)
        Button(master, width=11, height=4, text=')', relief='flat', bg='white', command=lambda: self.show(')')).grid(
            row=1, column=1)
        Button(master, width=11, height=4, text='%', relief='flat', bg='white', command=lambda: self.show('%')).grid(
            row=1, column=2)
        Button(master, width=11, height=4, text='C', relief='flat', bg='white', command=self.clear).grid(row=1,
                                                                                                         column=3)

        Button(master, width=11, height=4, text='1', relief='flat', bg='white', command=lambda: self.show('1')).grid(
            row=2, column=0)
        Button(master, width=11, height=4, text='2', relief='flat', bg='white', command=lambda: self.show('2')).grid(
            row=2, column=1)
        Button(master, width=11, height=4, text='3', relief='flat', bg='white', command=lambda: self.show('3')).grid(
            row=2, column=2)
        Button(master, width=11, height=4, text='/', relief='flat', bg='white', command=lambda: self.show('/')).grid(
            row=2, column=3)

        Button(master, width=11, height=4, text='4', relief='flat', bg='white', command=lambda: self.show('4')).grid(
            row=3, column=0)
        Button(master, width=11, height=4, text='5', relief='flat', bg='white', command=lambda: self.show('5')).grid(
            row=3, column=1)
        Button(master, width=11, height=4, text='6', relief='flat', bg='white', command=lambda: self.show('6')).grid(
            row=3, column=2)
        Button(master, width=11, height=4, text='*', relief='flat', bg='white', command=lambda: self.show('*')).grid(
            row=3, column=3)

        Button(master, width=11, height=4, text='7', relief='flat', bg='white', command=lambda: self.show('7')).grid(
            row=4, column=0)
        Button(master, width=11, height=4, text='8', relief='flat', bg='white', command=lambda: self.show('8')).grid(
            row=4, column=1)
        Button(master, width=11, height=4, text='9', relief='flat', bg='white', command=lambda: self.show('9')).grid(
            row=4, column=2)
        Button(master, width=11, height=4, text='-', relief='flat', bg='white', command=lambda: self.show('-')).grid(
            row=4, column=3)

        Button(master, width=11, height=4, text='0', relief='flat', bg='white', command=lambda: self.show('0')).grid(
            row=5, column=0)
        Button(master, width=11, height=4, text='.', relief='flat', bg='white', command=lambda: self.show('.')).grid(
            row=5, column=1)
        Button(master, width=11, height=4, text='+', relief='flat', bg='white', command=lambda: self.show('+')).grid(
            row=5, column=2)
        Button(master, width=11, height=4, text='=', relief='flat', bg='white', command=self.solve).grid(row=5,
                                                                                                         column=3)

    def show(self, value):
        self.entry_value += str(value)
        self.equation.set(self.entry_value)

    def clear(self):
        self.entry_value = ''
        self.equation.set(self.entry_value)

    def solve(self):
        try:
            result = eval(self.entry_value)
            self.equation.set(result)
        except Exception as e:
            print("Error:", e)
            self.equation.set("Error")


Root = Tk()
calculator = Calculator(Root)
Root.mainloop()
