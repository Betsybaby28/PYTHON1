f_obj=open("trial.txt",'w')
print(f_obj.tell())
f_obj.write("hello")
print(f_obj.tell())
f_obj.seek(3)
f_obj.write("python")

