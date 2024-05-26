from tkinter import *

action = ''
prices_food = [1.32, 1.65, 2.31, 3.22, 1.22, 1.99, 2.05, 2.65]
prices_drinks = [0.25, 0.99, 1.21, 1.54, 1.08, 1.10, 2.00, 1.58]
prices_desserts = [1.54, 1.68, 1.32, 1.97, 2.55, 2.14, 1.94, 1.74]

def click_button(number):
    global action
    action = action + number
    screen_calculator.delete(0, END)
    screen_calculator.insert(END, action)

def delete():
    global action
    action = ''
    screen_calculator.delete(0, END)

def get_result():
    global action
    result = str(eval(action))
    screen_calculator.delete(0, END)
    screen_calculator.insert(0, result)
    action = ''

def check():
    f = 0
    for i in inputs_food:
        if variables_food[f].get() == 1:
            inputs_food[f].config(state=NORMAL)
            if inputs_food[f].get() == '0':
                inputs_food[f].delete(0, END)
            inputs_food[f].focus()
        else:
            inputs_food[f].config(state=DISABLED)
            text_food[f].set('0')
        f += 1

    d = 0
    for i in inputs_drinks:
        if variables_drinks[d].get() == 1:
            inputs_drinks[d].config(state=NORMAL)
            if inputs_drinks[d].get() == '0':
                inputs_drinks[d].delete(0, END)
            inputs_drinks[d].focus()
        else:
            inputs_drinks[d].config(state=DISABLED)
            text_drinks[d].set('0')
        d += 1

    ds = 0
    for i in inputs_desserts:
        if variables_desserts[ds].get() == 1:
            inputs_desserts[ds].config(state=NORMAL)
            if inputs_desserts[ds].get() == '0':
                inputs_desserts[ds].delete(0, END)
            inputs_desserts[ds].focus()
        else:
            inputs_desserts[ds].config(state=DISABLED)
            text_desserts[ds].set('0')
        ds += 1

def total():
    sub_total_food = 0
    p = 0
    for quantity in text_food:
        sub_total_food = sub_total_food + (float(quantity.get()) * prices_food[p])
        p += 1

    sub_total_drinks = 0
    p = 0
    for quantity in text_drinks:
        sub_total_drinks = sub_total_drinks + (float(quantity.get()) * prices_drinks[p])
        p += 1

    sub_total_desserts = 0
    p = 0
    for quantity in text_desserts:
        sub_total_desserts = sub_total_desserts + (float(quantity.get()) * prices_desserts[p])
        p += 1

    sub_total = sub_total_food + sub_total_drinks + sub_total_desserts
    taxes = sub_total * 0.07
    total = sub_total + taxes

    var_cost_food.set(f'€ {round(sub_total_food, 2)}')
    var_cost_drinks.set(f'€ {round(sub_total_drinks, 2)}')
    var_cost_desserts.set(f'€ {round(sub_total_desserts, 2)}')
    var_subtotal.set(f'€ {round(sub_total, 2)}')
    var_tax.set(f'€ {round(taxes, 2)}')
    var_total.set(f'€ {round(total, 2)}')

# TKinter initialization and settings
app = Tk()

app.geometry('1280x630+0+0')

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
panel_costs = Frame(panel_left, bd=1, relief=FLAT, bg="chocolate2", padx=130)
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
                       onvalue=1, offvalue=0, variable=variables_food[count], command=check)

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
                       onvalue=1, offvalue=0, variable=variables_drinks[count], command=check)

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
                       onvalue=1, offvalue=0, variable=variables_desserts[count], command=check)

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
text_cost_food.grid(row=0, column=1, padx= 35)

tag_cost_drinks = Label(panel_costs, text='Cost drinks', font=('Arial', 12, 'bold'), bg="chocolate2", fg="white")
tag_cost_drinks.grid(row=1, column=0)

text_cost_drinks = Entry(panel_costs, font=('Arial', 12, 'bold'), bd=1, width=10,
                       state='readonly', textvariable=var_cost_drinks)
text_cost_drinks.grid(row=1, column=1, padx= 35)

tag_cost_desserts = Label(panel_costs, text='Cost desserts', font=('Arial', 12, 'bold'), bg="chocolate2", fg="white")
tag_cost_desserts.grid(row=2, column=0)

text_cost_desserts = Entry(panel_costs, font=('Arial', 12, 'bold'), bd=1, width=10,
                       state='readonly', textvariable=var_cost_desserts)
text_cost_desserts.grid(row=2, column=1, padx= 35)

tag_subtotal = Label(panel_costs, text='Subtotal', font=('Arial', 12, 'bold'), bg="chocolate2", fg="white")
tag_subtotal.grid(row=0, column=2)

text_subtotal = Entry(panel_costs, font=('Arial', 12, 'bold'), bd=1, width=10,
                       state='readonly', textvariable=var_subtotal)
text_subtotal.grid(row=0, column=3, padx= 35)

tag_tax = Label(panel_costs, text='Tax', font=('Arial', 12, 'bold'), bg="chocolate2", fg="white")
tag_tax.grid(row=1, column=2)

text_tax = Entry(panel_costs, font=('Arial', 12, 'bold'), bd=1, width=10,
                       state='readonly', textvariable=var_tax)
text_tax.grid(row=1, column=3, padx= 35)

tag_total = Label(panel_costs, text='Total', font=('Arial', 12, 'bold'), bg="chocolate2", fg="white")
tag_total.grid(row=2, column=2)

text_total = Entry(panel_costs, font=('Arial', 12, 'bold'), bd=1, width=10,
                       state='readonly', textvariable=var_total)
text_total.grid(row=2, column=3, padx= 35)

# Buttons
buttons = ['total', 'receipt', 'save', 'reset']
buttons_created = []
columns = 0

for button in buttons:
    button = Button(panel_buttons, text=button.title(), font=('Arial', 16, 'bold'),
                   fg="white", bg="blue", bd=1, width=9)

    buttons_created.append(button)

    button.grid(row=0, column=columns)
    columns += 1

buttons_created[0].config(command=total)

# Receipt
text_receipt = Text(panel_receipt, font=('Arial', 14, 'bold'), bd=1, width=45, height=10)
text_receipt.grid(row=0, column=0)

# Calculator
screen_calculator = Entry(panel_calculator, font=('Arial', 16, 'bold'), bd=1, width=42)
screen_calculator.grid(row=0, column=0, columnspan=6)

buttons_calculator = ['7', '8', '9', '+', '4', '5', '6', '-',
                      '1', '2', '3', 'x', '=', 'DEL', '0', '/']

saved_buttons = []

row = 1
column = 0

for button in buttons_calculator:
    button = Button(panel_calculator, text=button.title(), font=('Arial', 16, 'bold'),
                    fg="white", bg="blue", bd=1, width=9)
    saved_buttons.append(button)
    button.grid(row=row, column=column)

    if column == 3:
        row += 1

    column += 1

    if column == 4:
        column = 0

saved_buttons[0].config(command=lambda : click_button('7'))
saved_buttons[1].config(command=lambda : click_button('8'))
saved_buttons[2].config(command=lambda : click_button('9'))
saved_buttons[3].config(command=lambda : click_button('+'))
saved_buttons[4].config(command=lambda : click_button('4'))
saved_buttons[5].config(command=lambda : click_button('5'))
saved_buttons[6].config(command=lambda : click_button('6'))
saved_buttons[7].config(command=lambda : click_button('-'))
saved_buttons[8].config(command=lambda : click_button('1'))
saved_buttons[9].config(command=lambda : click_button('2'))
saved_buttons[10].config(command=lambda : click_button('3'))
saved_buttons[11].config(command=lambda : click_button('*'))
saved_buttons[12].config(command=get_result)
saved_buttons[13].config(command=delete)
saved_buttons[14].config(command=lambda : click_button('0'))
saved_buttons[15].config(command=lambda : click_button('/'))

# Prevents screen from closing
app.mainloop()