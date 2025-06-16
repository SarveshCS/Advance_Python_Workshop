from PIL import ImageTk, Image
from tkinter import Tk, Frame, Label

root = Tk()

frame = Frame(root, width=400, height=400)
frame.place(anchor='center', relx=0.5, rely=0.5)
frame.pack()

img_path = r"E:\Programming\college_workshop\1st_Year\Advance_Python_Workshop\Day_6\GUI\pillow\image.ico"
img = ImageTk.PhotoImage(Image.open(img_path))
label = Label(frame, image=img)
label.pack()
root.mainloop()