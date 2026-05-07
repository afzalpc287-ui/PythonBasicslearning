#conditional statement
#1st condition
light=input("light:")
if(light=="red"):
     print("stop")
elif(light=="green"):
     print("go")
elif(light=="yellow"):
     print("ready")
else:
     print("light is broken")
#2nd condition
marks = int(input("marks:"))
if(marks >= 90):
     print("a grade")
elif(marks >= 80 and marks < 90):
     print("b grade")
elif(marks >= 70 and marks <80):
     print("c grade")
else:
     print("Fail")  
#3rd condition
age=int(input("age:"))
if(age >=18):
     print("vote")
elif(age<18):
     print("under age")    
else:
     print("no vote")         
#one line statement
var=input("food:")
eat="yes"if var =="cake"else"no" 
print(eat)
#practice questions
#wap to check if a number entered by the user is odd or even
num=int(input("enter no:"))
rem=num % 2
if(rem == 0):
     print("the number is even") 
else:
     print("number is odd")     
#wap to find the greatest of 3 numbers entered by user
a=int(input("enter nums:"))
b=int(input("enter nums:"))
c=int(input("enter nums:"))
if(a>b and a>c):
     print("a")
elif(b>a and b>c):
     print("b")
elif(c>a and c>b):
     print("c")
else:
     print("recheck numbers") 
#wap to check if a number is a mutiple of 7 or not
num=int(input("enter num:"))
mul=num%7
if(mul==0):
    print(num,"  is mul by 7")
else:
    print(num,"  is not mul by 7") 
#wap to find the greatest of 4 numbers entered by user 
a=int(input("enter a:"))
b=int(input("enter b:"))
c=int(input("enter c:"))
d=int(input("enter d:"))
if(a>b and a>c and a>d):
     print("a is greatest:",a)
elif(b>a and b>c and b>d):
     print("b is grestest:",b)      
elif(c>a and c>b and c>d):
     print("c is greatest:",c)
else:
     print("d is greates:",d)


