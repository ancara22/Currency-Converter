from tkinter import *
from time import strftime

window = Tk()
window.title("Clock")
window.config(bg="black")
window.geometry("500x250")

lbl = Label(window, bg="black", fg="white", font="Arial 64 bold")
lbl.pack(anchor="center", expand=1)


def time():
    curent_time = strftime("%H %M %S %p")
    lbl.config(text=curent_time)
    lbl.after(1000, time)


time()
mainloop()
