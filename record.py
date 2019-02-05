print("DMC")
x=input("Enter Student Name ")
print("Enter Your Subjects And Marks Below")
a=input("Subject= ")
b=input("Marks= ")
c=input("Subject= ")
d=input("Marks= ")
e=input("Subject= ")
f=input("Marks= ")
g=input("Subject= ")
h=input("Marks= ")
i=input("subject= ")
j=input("Marks= ")
Marks1=int(b)
Marks2=int(d)
Marks3=int(f)
Marks4=int(h)
Marks5=int(j)
sum=Marks1+Marks2+Marks3+Marks4+Marks5
p=(sum/500)*100
print("You Percentage is",p)
if(p>90 and p<=100):
    print("You Have Got Grade A,Outstanding")
elif(p>80 and p<=90):
    print("You Have Got Grade B,Excellent")
elif(p>70 and p<=80):
    print("You Have Got Grade C,Good")
elif(p>60 and p<=70):
    print("You Have Got Grade D,Keep It Up")
elif(p>50 and p<=60):
    print("You Have Got Grade E,Can Do Better")
elif(p>40 and p<=50):
    print("You Have Got Grade P,Improve Yourself")
else:
    print("Try Harder")
    





