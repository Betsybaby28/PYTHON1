import tkinter as tk
root=tk.Tk()
root.geometry("600x400")
root.title("demo")
row_1=tk.Frame(root)
row_2=tk.Frame(root)
row_3=tk.Frame(root)
#row_1
button_1=tk.Button(row_1,text="button1",fg="blue",bg="yellow")
button_2=tk.Button(row_1,text="button2",fg="blue",bg="yellow")
button_3=tk.Button(row_1,text="button3",fg="blue",bg="yellow")
button_1.pack(side="left",padx=10,pady=10)
button_2.pack(side="left",padx=10,pady=10)
button_3.pack(padx=10,pady=10)
#row_2
row_1.pack(side="top")
button_4=tk.Button(row_2,text="button4",fg="blue",bg="yellow")
button_5=tk.Button(row_2,text="button5",fg="blue",bg="yellow")
button_6=tk.Button(row_2,text="button6",fg="blue",bg="yellow")
button_4.pack(side="left",padx=10,pady=10)
button_5.pack(side="left",padx=10,pady=10)
button_6.pack(padx=10,pady=10)
row_2.pack()
#row_3
button_7=tk.Button(row_3,text="button7",fg="blue",bg="yellow")
button_8=tk.Button(row_3,text="button8",fg="blue",bg="yellow")
button_9=tk.Button(row_3,text="button9",fg="blue",bg="yellow")
button_7.pack(side="left",padx=10,pady=10)
button_8.pack(side="left",padx=10,pady=10)
button_9.pack(padx=10,pady=10)
row_3.pack()
root.mainloop()
