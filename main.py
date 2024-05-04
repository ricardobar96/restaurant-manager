from tkinter import *

# TKinter initialization and settings
app = Tk()

app.geometry('1020x630+0+0')

app.resizable(0, 0)

app.title("Restaurant Manager - Ricardo Baloira Armas")

app.config(background='seashell3')

# Top panel
panel_top = Frame(app, bd=1, relief=FLAT)
panel_top.pack(side=TOP)

# Tag title
tag_title = Label(panel_top, text='Restaurant Manager', fg='chocolate2',
                  font=('Arial', 50), bg='seashell3', width=20)

tag_title.grid(row=0, column=0)

# Left panel
panel_left = Frame(app, bd=1, relief=FLAT)
panel_left.pack(side=LEFT)

# Costs panel
panel_costs = Frame(panel_left, bd=1, relief=FLAT)
panel_costs.pack(side=BOTTOM)

# Food panel
panel_food = LabelFrame(panel_left, text='Food', fg='chocolate4',
                  font=('Arial', 20, 'bold'), relief=FLAT, bd=1)

panel_food.pack(side=LEFT)

# Drinks panel
panel_drinks = LabelFrame(panel_left, text='Drinks', fg='chocolate4',
                  font=('Arial', 20, 'bold'), relief=FLAT, bd=1)

panel_drinks.pack(side=LEFT)

# Desserts panel
panel_desserts = LabelFrame(panel_left, text='Desserts', fg='chocolate4',
                  font=('Arial', 20, 'bold'), relief=FLAT, bd=1)

panel_desserts.pack(side=LEFT)

# Right panel
panel_right = Frame(app, bd=1, relief=FLAT)
panel_right.pack(side=RIGHT)

# Calculator panel
panel_calculator = Frame(panel_right, bd=1, relief=FLAT, bg='seashell3')
panel_calculator.pack()

# Calculator receipt
panel_receipt = Frame(panel_right, bd=1, relief=FLAT, bg='seashell3')
panel_receipt.pack()

# Buttons panel
panel_buttons = Frame(panel_right, bd=1, relief=FLAT, bg='seashell3')
panel_buttons.pack()

# Prevents screen from closing
app.mainloop()