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

# Lists
list_food = ['Pizza', 'Chicken', 'Beef', 'Fish', 'Fries', 'Burger', 'Salad', 'Sandwich']
list_drinks = ['Water', 'Lemonade', 'Beer', 'Wine', 'Coffee', 'Tea', 'Juice', 'Soda']
list_desserts = ['Cake', 'Donut', 'Fruit', 'Cookies', 'Croissant', 'Muffin', 'Waffle', 'Mousse']

# Items food
variables_food = []
inputs_food = []
text_food = []
count = 0

for food in list_food:

    # Create checkbuttons
    variables_food.append('')
    variables_food[count] = IntVar()
    food = Checkbutton(panel_food, text=food.title(), font=('Arial', 20, 'bold'),
                       onvalue=1, offvalue=0, variable=variables_food[count])

    food.grid(row=count, column=0, sticky=W)

    # Create inputs
    inputs_food.append('')
    text_food.append('')
    text_food[count] = StringVar()
    text_food[count].set('0')
    inputs_food[count] = Entry(panel_food, font=('Arial', 19, 'bold'),
                       bd=1, width=6, state=DISABLED, textvariable=text_food[count])

    inputs_food[count].grid(row=count, column=1)

    count += 1

# Items drinks
variables_drinks = []
inputs_drinks = []
text_drinks = []
count = 0

for drink in list_drinks:

    # Create checkbuttons
    variables_drinks.append('')
    variables_drinks[count] = IntVar()
    drink = Checkbutton(panel_drinks, text=drink.title(), font=('Arial', 20, 'bold'),
                       onvalue=1, offvalue=0, variable=variables_drinks[count])

    drink.grid(row=count, column=0, sticky=W)

    # Create inputs
    inputs_drinks.append('')
    text_drinks.append('')
    text_drinks[count] = StringVar()
    text_drinks[count].set('0')
    inputs_drinks[count] = Entry(panel_drinks, font=('Arial', 19, 'bold'),
                               bd=1, width=6, state=DISABLED, textvariable=text_drinks[count])

    inputs_drinks[count].grid(row=count, column=1)

    count += 1

# Items desserts
variables_desserts = []
inputs_desserts = []
text_desserts = []
count = 0

for dessert in list_desserts:

    # Create checkbuttons
    variables_desserts.append('')
    variables_desserts[count] = IntVar()
    dessert = Checkbutton(panel_desserts, text=dessert.title(), font=('Arial', 20, 'bold'),
                       onvalue=1, offvalue=0, variable=variables_desserts[count])

    dessert.grid(row=count, column=0, sticky=W)

    # Create inputs
    inputs_desserts.append('')
    text_desserts.append('')
    text_desserts[count] = StringVar()
    text_desserts[count].set('0')
    inputs_desserts[count] = Entry(panel_desserts, font=('Arial', 19, 'bold'),
                               bd=1, width=6, state=DISABLED, textvariable=text_desserts[count])

    inputs_desserts[count].grid(row=count, column=1)

    count += 1

# Variables
var_cost_food = StringVar()
var_cost_drinks = StringVar()
var_cost_desserts = StringVar()
var_tax = StringVar()
var_subtotal = StringVar()
var_total = StringVar()

# Costs tags and input fields
tag_cost_food = Label(panel_costs, text='Cost food', font=('Arial', 12, 'bold'), bg="chocolate2", fg="white")
tag_cost_food.grid(row=0, column=0)

text_cost_food = Entry(panel_costs, font=('Arial', 12, 'bold'), bd=1, width=10,
                       state='readonly', textvariable=var_cost_food)
text_cost_food.grid(row=0, column=1)

tag_cost_drinks = Label(panel_costs, text='Cost drinks', font=('Arial', 12, 'bold'), bg="chocolate2", fg="white")
tag_cost_drinks.grid(row=1, column=0)

text_cost_drinks = Entry(panel_costs, font=('Arial', 12, 'bold'), bd=1, width=10,
                       state='readonly', textvariable=var_cost_drinks)
text_cost_drinks.grid(row=1, column=1)

tag_cost_desserts = Label(panel_costs, text='Cost desserts', font=('Arial', 12, 'bold'), bg="chocolate2", fg="white")
tag_cost_desserts.grid(row=2, column=0)

text_cost_desserts = Entry(panel_costs, font=('Arial', 12, 'bold'), bd=1, width=10,
                       state='readonly', textvariable=var_cost_desserts)
text_cost_desserts.grid(row=2, column=1)

tag_subtotal = Label(panel_costs, text='Subtotal', font=('Arial', 12, 'bold'), bg="chocolate2", fg="white")
tag_subtotal.grid(row=0, column=2)

text_subtotal = Entry(panel_costs, font=('Arial', 12, 'bold'), bd=1, width=10,
                       state='readonly', textvariable=var_subtotal)
text_subtotal.grid(row=0, column=3)

tag_tax = Label(panel_costs, text='Tax', font=('Arial', 12, 'bold'), bg="chocolate2", fg="white")
tag_tax.grid(row=1, column=2)

text_tax = Entry(panel_costs, font=('Arial', 12, 'bold'), bd=1, width=10,
                       state='readonly', textvariable=var_tax)
text_tax.grid(row=1, column=3)

# Prevents screen from closing
app.mainloop()