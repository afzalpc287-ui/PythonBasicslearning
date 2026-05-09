#functions
def calcu_sum(a,b):
    sum=a+b
    print(sum)
    return sum
#multiple lines of code
calcu_sum(2,3)
#multiple lines of code
calcu_sum(200,300)
#multiple lines of code
calcu_sum(100,300)
#multiple lines of code
calcu_sum(4000,5000)
#multiple lines of code
calcu_sum(53,524)
#for string syntax
def print_hello():
    print("hello")
#lines of code
print_hello()
print_hello()
print_hello()
print_hello()
#3 numbers avg
def calcu_avg(a,b,c):
    sum=a+b+c
    avg=sum/3
    print(avg)
    return avg
#lines of code
calcu_avg(1,2,3)
#perameters
def cal_m(a=2,b=7):
    m= a*b
    print(m)
    return m
#line of code
cal_m(2,4)
#practice questions
#wap to print the length of a list.(list is the parameter)
list =["abdul","sahil","mubbi","suhaib","amjad","afzal"]
def cal_list (list):
    print(len(list))
#lines of code
cal_list(list)
#waf to print the elements of a list in a single line.(lis is the parameter)
list1 =["abdul","sahil","mubbi","suhaib","amjad","afzal"]
list2 =["abdul","sahil","mubbi","suhaib","amjad","afzal"]
def cal_list2(list):
    for item in list:
        print(item,end=" ")
cal_list2(list2)       
#waf to find the factorial of n.(n is the parammeter)
n = int (input("enter n:"))
fact = 1
for i in range(1, n+1):
    fact*=i
    print(fact)
#waf to covert usd to inr
def converter(a,b=83):
    con =a*b
    print(con)
    return con
#lines of code
converter(45)
#home work problem
def home(a,b=2):
    rem=b/a
    if(rem==True):
        print("EVEN")
    else:
        print("ODD")    
#while no of code  
home(int(input("enter a:")))           
#recursion function
def rec(n):
    if (n==0):
        return
    print(n)
    rec(n-1)
#while of code
rec(5) 
#recursion of factorial
def fac(n):
    if(n==1 or n==0):
        return 1
    return fac(n-1)*n
#while of code
print(fac(6))
#waf to calculate the sum of first n natural numbers.
def sum(n):
    if(n==0):
        return 0
    return sum(n-1)+n
print(sum(5))   
#waf to print all elements in a list. (HINT:-use list and index as parameters)
def q2(list,index=0):
    if(index==len(list)):
        return 
    print(list[index])
    q2(list,index+1)
fruits =["mango","apple","banana"]
q2(fruits)
