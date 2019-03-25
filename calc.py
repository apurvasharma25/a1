from tkinter import *
root=Tk()
root.title("Calculator")
root.resizable(1,1)
root.wm_attributes("-topmost",1)

Label1=Label(root,text="calculator app")
Label1.grid(row=0,columnspan=8)

equa=""
equation=StringVar()
calculation=Label(root,textvariable=equation)
equation.set("Enter Your Expression :")
calculation.grid(row=2,columnspan=8)

def btnPress(num):
    global equa
    equa=equa+str(num)
    equation.set(equa)

def EqualPress():
    global equa
    total=str(eval(equa))
    equation.set(total)
    equa=""

def ClearPress():
    global equa
    equa=""
    equation.set("")


a=Button(root,text="0",command=lambda:btnPress(1),borderwidth=1,relief=SOLID,fg="white",bg="#A1CD54")
a.grid(row=6,column=2,padx=10,pady=10)

b=Button(root,text="1",command=lambda:btnPress(1),borderwidth=1,relief=SOLID,fg="white",bg="#A1CD54")
b.grid(row=3,column=1,padx=10,pady=10)

c=Button(root,text="2",command=lambda:btnPress(2),borderwidth=1,relief=SOLID,fg="white",bg="#A1CD54")
c.grid(row=3,column=2,padx=10,pady=10)

d=Button(root,text="3",command=lambda:btnPress(3),borderwidth=1,relief=SOLID,fg="white",bg="#A1CD54")
d.grid(row=3,column=3,padx=10,pady=10)

e=Button(root,text="4",command=lambda:btnPress(4),borderwidth=1,relief=SOLID,fg="white",bg="#A1CD54")
e.grid(row=4,column=1,padx=10,pady=10)

f=Button(root,text="5",command=lambda:btnPress(5),borderwidth=1,relief=SOLID,fg="white",bg="#A1CD54")
f.grid(row=4,column=2,padx=10,pady=10)

g=Button(root,text="6",command=lambda:btnPress(6),borderwidth=1,relief=SOLID,fg="white",bg="#A1CD54")
g.grid(row=4,column=3,padx=10,pady=10)

h=Button(root,text="7",command=lambda:btnPress(7),borderwidth=1,relief=SOLID,fg="white",bg="#A1CD54")
h.grid(row=5,column=1,padx=10,pady=10)

i=Button(root,text="8",command=lambda:btnPress(8),borderwidth=1,relief=SOLID,fg="white",bg="#A1CD54")
i.grid(row=5,column=2,padx=10,pady=10)

j=Button(root,text="9",command=lambda:btnPress(9),borderwidth=1,relief=SOLID,fg="white",bg="#A1CD54")
j.grid(row=5,column=3,padx=10,pady=10)

plus=Button(root,text="+",command=lambda:btnPress("+"),borderwidth=1,relief=SOLID,fg="white",bg="#A1CD54")
plus.grid(row=3,column=4,padx=10,pady=10)

minus=Button(root,text="-",command=lambda:btnPress("-"),borderwidth=1,relief=SOLID,fg="white",bg="#A1CD54")
minus.grid(row=4,column=4,padx=10,pady=10)

multiply=Button(root,text="*",command=lambda:btnPress("*"),borderwidth=1,relief=SOLID,fg="white",bg="#A1CD54")
multiply.grid(row=5,column=4,padx=10,pady=10)

divide=Button(root,text="/",command=lambda:btnPress("/"),borderwidth=1,relief=SOLID,fg="white",bg="#A1CD54")
divide.grid(row=6,column=4,padx=10,pady=10)

equal=Button(root,text="=",command=lambda:EqualPress(),borderwidth=1,relief=SOLID,fg="white",bg="#A1CD54")
equal.grid(row=6,column=3,padx=10,pady=10)

clear=Button(root,text="C",command=lambda:ClearPress(),borderwidth=1,relief=SOLID,fg="white",bg="#A1CD54")
clear.grid(row=6,column=1,padx=10,pady=10)

root.mainloop()
