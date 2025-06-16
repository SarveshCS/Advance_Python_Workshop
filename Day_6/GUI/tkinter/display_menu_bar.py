from tkinter import Tk, Menu

root = Tk()
root.geometry("600x500+300+150")
root.configure(background='#5b5b5b')

menubar = Menu(root)

fileMenu = Menu(root, tearoff=0)

fileMenu.add_command(label="Stop", command=root.destroy)
fileMenu.add_command(label="Kill", command=root.destroy)
fileMenu.add_command(label="Exit", command=root.destroy)

menubar.add_cascade(label='File', menu=fileMenu)
root.config(menu=menubar)

root.mainloop()