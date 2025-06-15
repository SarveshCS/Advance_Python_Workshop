from tkinter import * 
root=Tk()

dark_bg = "#c5c5c5"
dark_text = "#58595c"
dark_accent ="#e3e3e3"


root.title("Login")
root.config(background=dark_bg)

inner=Frame(root, width=100, bd=0, relief=RIDGE)
inner.pack()

username_lbl = Label(inner, text="Username")
username_lbl.pack()

username=Entry(inner, width=75, borderwidth=0)
username.grid(row=0, column=0, columnspan=4, padx=5, pady=5)

passqord_lbl = Label(inner, text="Password")
passqord_lbl.pack()

password=Entry(inner, width=75, borderwidth=0)
password.grid(row=1, column=0, columnspan=4, padx=5, pady=5)

button_1=Button(inner, text='1', bd=1, padx=30, pady=10, relief=RIDGE, font=15, width=4)
button_2=Button(inner, text='2', bd=1, padx=30, pady=10, relief=RIDGE, font=15, width=4)
button_3=Button(inner, text='3', bd=1, padx=30, pady=10, relief=RIDGE, font=15, width=4)
button_4=Button(inner, text='4', bd=1, padx=30, pady=10, relief=RIDGE, font=15, width=4)
button_5=Button(inner, text='5', bd=1, padx=30, pady=10, relief=RIDGE, font=15, width=4)
button_6=Button(inner, text='6', bd=1, padx=30, pady=10, relief=RIDGE, font=15, width=4)
button_7=Button(inner, text='7', bd=1, padx=30, pady=10, relief=RIDGE, font=15, width=4)
button_8=Button(inner, text='8', bd=1, padx=30, pady=10, relief=RIDGE, font=15, width=4)
button_9=Button(inner, text='9', bd=1, padx=30, pady=10, relief=RIDGE, font=15, width=4)
button_0=Button(inner, text='0', bd=1, padx=30, pady=10, relief=RIDGE, font=15, width=4)

                    
## color setting
button_1.config(background=dark_bg, foreground=dark_text)
button_2.config(background=dark_bg, foreground=dark_text)
button_3.config(background=dark_bg, foreground=dark_text)
button_4.config(background=dark_bg, foreground=dark_text)
button_5.config(background=dark_bg, foreground=dark_text)
button_6.config(background=dark_bg, foreground=dark_text)
button_7.config(background=dark_bg, foreground=dark_text)
button_8.config(background=dark_bg, foreground=dark_text)
button_9.config(background=dark_bg, foreground=dark_text)
button_0.config(background=dark_bg, foreground=dark_text)


button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)
button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)

root.mainloop()