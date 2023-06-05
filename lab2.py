# lab 2
from tkinter import *


def calculate():
    a = txt_a.get()
    b = txt_b.get()
    e = int(a) % int(b)
    label = Label(window, text=e)
    label.grid(column=0, row=6)


window = Tk()
window.title("a mod b")
window.geometry('400x250')
lbl = Label(window, text="c = a mod b")
lbl.grid(column=0, row=0)
lbl = Label(window, text="a=")
lbl.grid(column=0, row=1)
lbl = Label(window, text="b=")
lbl.grid(column=0, row=2)
txt_a = Entry(window, width=10)
txt_a.grid(column=1, row=1)
txt_b = Entry(window, width=10)
txt_b.grid(column=1, row=2)
btn = Button(window, text="Result", command=calculate)
btn.grid(column=0, row=5)
if __name__ == "__main__":
    window.mainloop()
