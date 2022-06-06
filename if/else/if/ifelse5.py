m=int(input("enter the marks"))
if m>80:
    print("A grade")
elif m<80 and m>60:
    print("B grade")
elif m<60 and m>50:
    print("C grade")
elif m<50 and m>45:
    print("D grade")
elif m<45 and m>25:
    print("E grade")
else:
    print("F grade")