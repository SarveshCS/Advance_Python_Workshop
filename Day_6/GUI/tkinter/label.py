from tkinter import Tk, Label

root = Tk()
root.geometry("600x500+300+150")
msg = Label(root, text="Welcome to workshop")
msg.pack()
root.mainloop()