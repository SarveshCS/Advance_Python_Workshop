from tkinter import Tk, Label

root = Tk()
root.geometry("600x500+300+150")
root.configure(background='#5b5b5b')
msg = Label(root, text="""Welcome to workshop!""", background="#9a9999")
msg.config(font=('Times new roman', 33, 'italic bold'), foreground='#f7f7f7')
msg.pack()
root.mainloop()