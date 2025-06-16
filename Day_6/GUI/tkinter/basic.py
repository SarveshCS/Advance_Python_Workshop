from tkinter import Tk

root = Tk()
sw = root.winfo_screenwidth()
sh = root.winfo_screenheight()
print(sw, sh)
root.title("Welcome to the workshop")
root.mainloop()