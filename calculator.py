import tkinter as tk


root = tk.Tk()
root.title("Calculator")
root.resizable(width=False, height=False)
POWER_ON = False

# rows
row_0 = tk.Frame(root, )
row_1 = tk.Frame(root, )
row_2 = tk.Frame(root, )
row_3 = tk.Frame(root, )
row_4 = tk.Frame(root, )
row_5 = tk.Frame(root, )

# packing rows
row_0.pack()
row_1.pack()
row_2.pack()
row_3.pack()
row_4.pack()
row_5.pack()

# display
display = tk.Label(
    row_0, bg='darkgreen',
    height=3,
    width=13,
    anchor=tk.E,
    font=('bold', 18)
    )
display.grid(row=0, column=0, columnspan=4)

# functions

def toggle_power_state():
    global POWER_ON
    POWER_ON = not POWER_ON
    if POWER_ON == False:
        all_clear()
        display.config(bg='darkgreen')
    else:
        display.config(bg='lightgreen')
        update_display('0')

def update_display(text):
    if POWER_ON:
        curr_text = display.cget('text')
        if curr_text == '0':
            curr_text = ""
        new_text = curr_text + text
        display.config(text=new_text)
    else:
        print("Please power on the calculator! ")

def calculate():
    expression = display.cget('text')
    result = eval(expression)
    all_clear()
    update_display(str(result))

def all_clear():
    display.config(text="")

def clear_by_one():
    curr_text = display.cget('text')
    new_text = curr_text[:-1]
    all_clear()
    update_display(new_text)

# buttons
# row 1
btn_on_off = tk.Button(row_1, width=5, height=5, text='ON', command=toggle_power_state)
btn_ac = tk.Button(row_1, width=5, height=5, text='AC', command=all_clear)
btn_c = tk.Button(row_1, width=5, height=5, text='C', command=clear_by_one)
btn_percent = tk.Button(row_1, width=5, height=5, text='%', command=lambda : update_display('%'))

# packing buttons in row 1
btn_on_off.grid(row=1, column=0)
btn_ac.grid(row=1, column=1)
btn_c.grid(row=1, column=2)
btn_percent.grid(row=1, column=3)

# row 2
btn_1 = tk.Button(row_2, width=5, height=5, text='1', command=lambda : update_display('1'))
btn_2 = tk.Button(row_2, width=5, height=5, text='2', command=lambda : update_display('2'))
btn_3 = tk.Button(row_2, width=5, height=5, text='3', command=lambda : update_display('3'))
btn_plus = tk.Button(row_2, width=5, height=5, text='+', command=lambda : update_display('+'))

# packing buttons in row 2
btn_1.grid(row=2, column=0)
btn_2.grid(row=2, column=1)
btn_3.grid(row=2, column=2)
btn_plus.grid(row=2, column=3)

# row 3
btn_4 = tk.Button(row_3, width=5, height=5, text='4', command=lambda : update_display('4'))
btn_5 = tk.Button(row_3, width=5, height=5, text='5', command=lambda : update_display('5'))
btn_6 = tk.Button(row_3, width=5, height=5, text='6', command=lambda : update_display('6'))
btn_minus = tk.Button(row_3, width=5, height=5, text='-', command=lambda : update_display('-'))

# packing buttons in row 3
btn_4.grid(row=3, column=0)
btn_5.grid(row=3, column=1)
btn_6.grid(row=3, column=2)
btn_minus.grid(row=3, column=3)

# row 4
btn_7 = tk.Button(row_4, width=5, height=5, text='7', command=lambda : update_display('7'))
btn_8 = tk.Button(row_4, width=5, height=5, text='8', command=lambda : update_display('8'))
btn_9 = tk.Button(row_4, width=5, height=5, text='9', command=lambda : update_display('9'))
btn_mul = tk.Button(row_4, width=5, height=5, text='*', command=lambda : update_display('*'))

# packing buttons in row 4
btn_7.grid(row=4, column=0)
btn_8.grid(row=4, column=1)
btn_9.grid(row=4, column=2)
btn_mul.grid(row=4, column=3)

# row 5
btn_dot = tk.Button(row_5, width=5, height=5, text='.', command=lambda : update_display('.'))
btn_0 = tk.Button(row_5, width=5, height=5, text='0', command=lambda : update_display('0'))
btn_equal = tk.Button(row_5, width=5, height=5, text='=', command=calculate)
btn_div = tk.Button(row_5, width=5, height=5, text='/', command=lambda : update_display('/'))

# packing buttons in row 5
btn_dot.grid(row=5, column=0)
btn_0.grid(row=5, column=1)
btn_equal.grid(row=5, column=2)
btn_div.grid(row=5, column=3)




# binding functions to all buttons




if __name__ == "__main__":
    root.mainloop()