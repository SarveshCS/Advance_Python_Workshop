from tkinter import Tk, Label, Button

root = Tk()
root.geometry("600x500+300+150")

fontsize = 33

def increase():
    global fontsize
    fontsize+=2
    msg.config(font=('Times new roman', fontsize, 'italic bold'))

def decrease():
    global fontsize
    fontsize-=2
    msg.config(font=('Times new roman', fontsize, 'italic bold'))

incbtn = Button(root, text="A+", command=increase)
incbtn.pack()

decbtn = Button(root, text="A-", command=decrease)
decbtn.pack()

msg = Label(root, text="Welcome to workshop!")

msg.config(font=('Times new roman', fontsize, 'italic bold'),)
msg.pack()

root.mainloop()