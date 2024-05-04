from tkinter import *

app = Tk()

app.geometry('1020x630+0+0')

app.resizable(0, 0)

app.title("Restaurant Manager - Ricardo Baloira Armas")

app.config(background='seashell3')

panel_top = Frame(app, bd=1, relief=FLAT)
panel_top.pack(side=TOP)

tag_title = Label(panel_top, text='Restaurant Manager', fg='chocolate2',
                  font=('Arial', 50), bg='seashell3', width=20)

tag_title.place(x=.5, y=.5, anchor = "center")

tag_title.grid(row=0, column=0)

app.mainloop()