import tkinter as tk
root=tk.Tk()
root.geometry("600x400")
root.title("demo")

# rows
row_0=tk.Frame(root)
row_1=tk.Frame(root)
row_2=tk.Frame(root)
row_3=tk.Frame(root)
row_4=tk.Frame(root)





#display
display=tk.Label(row_0,bg="lightgreen",height=4, width=25)
display.grid(row=0,column=0,columnspan=4)

#row1
button_1=tk.Button(row_0,text="ON",fg="blue",bg="grey",width=5,height=4)
button_1.grid(row=1,column=0)
button_2=tk.Button(row_0,text="%",fg="blue",bg="grey",width=5,height=4)
button_2.grid(row=1,column=1)
button_3=tk.Button(row_0,text="X",fg="blue",bg="grey",width=5,height=4)
button_3.grid(row=1,column=2)
button_4=tk.Button(row_0,text="AC",fg="blue",bg="grey",width=5,height=4)
button_4.grid(row=1,column=3)
row_0.pack()

#row2
button_5=tk.Button(row_1,text="7",fg="blue",bg="grey",width=5,height=4)
button_5.grid(row=2,column=0)
button_6=tk.Button(row_1,text="8",fg="blue",bg="grey",width=5,height=4)
button_6.grid(row=2,column=1)
button_7=tk.Button(row_1,text="9",fg="blue",bg="grey",width=5,height=4)
button_7.grid(row=2,column=2)
button_8=tk.Button(row_1,text="/",fg="blue",bg="grey",width=5,height=4)
button_8.grid(row=2,column=3)
row_1.pack()

#row3
button_9=tk.Button(row_2,text="4",fg="blue",bg="grey",width=5,height=4)
button_9.grid(row=3,column=0)
button_10=tk.Button(row_2,text="5",fg="blue",bg="grey",width=5,height=4)
button_10.grid(row=3,column=1)
button_11=tk.Button(row_2,text="6",fg="blue",bg="grey",width=5,height=4)
button_11.grid(row=3,column=2)
button_12=tk.Button(row_2,text="*",fg="blue",bg="grey",width=5,height=4)
button_12.grid(row=3,column=3)
row_2.pack()

#row4
button_13=tk.Button(row_3,text="1",fg="blue",bg="grey",width=5,height=4)
button_13.grid(row=4,column=0)
button_14=tk.Button(row_3,text="2",fg="blue",bg="grey",width=5,height=4)
button_14.grid(row=4,column=1)
button_15=tk.Button(row_3,text="3",fg="blue",bg="grey",width=5,height=4)
button_15.grid(row=4,column=2)
button_16=tk.Button(row_3,text="-",fg="blue",bg="grey",width=5,height=4)
button_16.grid(row=4,column=3)
row_3.pack()

#row5
button_17=tk.Button(row_4,text="0",fg="blue",bg="grey",width=5,height=4)
button_17.grid(row=5,column=0)
button_18=tk.Button(row_4,text=".",fg="blue",bg="grey",width=5,height=4)
button_18.grid(row=5,column=1)
button_19=tk.Button(row_4,text="=",fg="blue",bg="grey",width=5,height=4)
button_19.grid(row=5,column=2)
button_20=tk.Button(row_4,text="+",fg="blue",bg="grey",width=5,height=4)
button_20.grid(row=5,column=3)
row_4.pack()
root.mainloop()

