from tkinter import Tk, Label, Button

root = Tk()
root.title("Calculator")
root.geometry("500x450+300+150")
root.configure(background='#5b5b5b')

output = Label(root, text="OUTPUT!")
output.pack(side="bottom")
output.place(relx=0, rely=0, relheight=0.1, relwidth=1)

msgbtn = Button(root, text="C")
msgbtn.pack(side="bottom")
output.place(relx=0, rely=0.1, relheight=0.1, relwidth=0.3)


# msg = Label(root, text="""Welcome to workshop!""", background="#9a9999")
# msg.config(font=('Times new roman', 33, 'italic bold'), foreground='#f7f7f7')
# msg.pack()

root.mainloop()