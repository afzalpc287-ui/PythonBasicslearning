# Query: #opeartors
#arithmatic operators
num1=int(input("num1:"))
num2=int(input("num2:"))
sum=num1+num2
mul=num1*num2
min=num2-num1
div=num2/num1
rem=num2%num1
power1= num1**num1
power2= num2**num2
print("sum:",sum)
print("mul:",mul)
print("min",min)
print("div:",div)
print("rem:",rem)
print("power1:",power1)
print("power2:",power2)
#relational operator
a=10
b=20
print(a!=b)
print(a>b)
print(a<b)
print(a>=b)
print(a<=b)
#logical operators
#not operator
a=input("a:")
b=input("b:")
c=a+b
print ("a=b:",(not True))
#or operator
val1=True
val2=False
print("or operater:",val1 or val2)
#and operator
val3=True
val4=True
print("and operator",val3 and val4)
#practice questions
#write a program to input 2 numbers and print their sum
num1=int(input("num1:"))
num2=int(input("num2:"))
print (num1+num2)
#wap to input side of a square and print its area
side1=int(input("side:"))
area=side1*side1
print(area)
#wap to input 2 floating point numbers and print their average
num1=float(input("num1:"))
num2=float(input("num2:"))
avg=(num1+num2)/2
print("avg:",avg)
"""wap to print 2 int numbers, a and b.
print true if a is grater than or equal to b. if not print false"""
a=int(input("a:"))
b=int(input("b:"))
print(a>=b)