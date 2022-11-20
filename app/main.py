from google_earth import showFlight
from tkinter import *
from threading import Thread
from time import sleep


def clicked():
    global txt
    global window

    t = Thread(target=showFlight, args=[txt.get()])
    t.start()

    sleep(5)

    window.withdraw()


if __name__=="__main__":

    window = Tk()

    window.title("Enter Flight :")

    window.geometry('350x200')

    lbl = Label(window)

    lbl.grid(column=0, row=0)

    txt = Entry(window,width=10)

    txt.grid(column=1, row=0)
    btn = Button(window, text="Click Me", command=clicked)

    btn.grid(column=2, row=0)

    window.mainloop()

