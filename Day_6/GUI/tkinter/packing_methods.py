from tkinter import Tk, Label

root = Tk()
root.geometry("600x500+300+150")
msg = Label(root, text="Welcome to workshop")
msg.config(font=('Times new roman', 33, 'italic bold underline'))
msg.pack(pady=10, ipadx=0, side='top')
root.mainloop()