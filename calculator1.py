import tkinter as tk
root = tk.Tk()
root.title("Calculator")
root.resizable(width=False, height=False)
POWER_ON = False

#rows
row_0=tk.Frame(root, )
row_1=tk.Frame(root, )
row_2=tk.Frame(root, )
row_3=tk.Frame(root, )
row_4=tk.Frame(root, )
row_5=tk.Frame(root, )

#packing rows
row_0.pack()
row_1.pack()
row_2.pack()
row_3.pack()
row_4.pack()
row_5.pack()


#display
display=tk.Label(row_0,bg="darkgreen",height=3,width=13,anchor=tk.E,font=('bold',18))
display.grid(row=0,column=0,columnspan=4)

#functions



#buttons
#row1
button_on_off=tk.Button(row_1,height=5,width=5,text="ON",command=toggle_power_state)
button_ac=tk.Button(row_1,height=5,width=5,text="AC",command=all_clear)
button_c=tk.Button(row_1,height=5,width=5,text="C",command=clear_by_one)
button_percent=tk.Button(row_1,height=5,width=5,text="%",command=lambda :update_display('%'))

#packing buttons in row1
button_on_off.grid(row=1,column=0)
button_ac.grid(row=1,column=1)
button_c.grid(row=1,column=2)
button_percent.grid(row=1,column=3)


#row2
button_1=tk.Button(row_2,height=5,width=5,text="1",command=lambda :update_display('1'))
button_2=tk.Button(row_2,height=5,width=5,text="2",command=lambda : update_display('2'))
button_3=tk.Button(row_2,height=5,width=5,text="3",command=lambda : update_display('3'))
button_plus=tk.Button(row_2,height=5,width=5,text="+",command=lambda : update_display('+'))

#packing buttons in row2
button_1.grid(row=2,column=0)
button_2.grid(row=2,column=1)
button_3.grid(row=2,column=2)
button_plus.grid(row=2,column=3)

#row3
button_4=tk.Button(row_3,height=5,width=5,text="4",command=lambda :update_display('4'))
button_5=tk.Button(row_3,height=5,width=5,text="5",command=lambda :update_display('5'))
button_6=tk.Button(row_3,height=5,width=5,text="6",command=lambda :update_display('6'))
button_minus=tk.Button(row_3,height=5,width=5,text="-",command=lambda :update_display('-'))

#packing buttons in row3
button_4.grid(row=3,column=0)
button_5.grid(row=3,column=1)
button_6.grid(row=3,column=2)
button_minus.grid(row=3,column=3)

#row4
button_7=tk.Button(row_4,height=5,width=5,text="7",command=lambda :update_display('7'))
button_8=tk.Button(row_4,height=5,width=5,text="8",command=lambda :update_display('8'))
button_9=tk.Button(row_4,height=5,width=5,text="9",command=lambda :update_display('9'))
button_mul=tk.Button(row_4,height=5,width=5,text="*",command=lambda :update_display('*'))

#packing buttons in row4
button_7.grid(row=4,column=0)
button_8.grid(row=4,column=1)
button_9.grid(row=4,column=2)
button_mul.grid(row=4,column=3)

#row5
button_0=tk.Button(row_5,height=5,width=5,text="0",command=lambda :update_display('0'))
button_dot=tk.Button(row_5,height=5,width=5,text=".",command=lambda :update_display('.'))
button_equal=tk.Button(row_5,height=5,width=5,text="=",command=lambda :update_display('='))
button_div=tk.Button(row_5,height=5,width=5,text="/",command=lambda :update_display('/'))

#packing buttons in row5
button_0.grid(row=5,column=0)
button_dot.grid(row=5,column=1)
button_equal.grid(row=5,column=2)
button_div.grid(row=5,column=3)

# binding functions to all buttons




if __name__ == "__main__":
    root.mainloop()







