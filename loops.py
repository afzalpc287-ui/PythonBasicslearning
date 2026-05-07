#loops in python
#while loop
count = 1
while count<=5:
    print("afzal",count)
count+= 1 
#practice questions for while loop
#wap to print numbers from 1 to 100
limit = 1
while limit<=100:
    print(limit)
    limit+=1
#wap to print numbers from 100 to 1
limit2 =100
while limit2>=1:
    print(limit2)
    limit2-=1
#wap to print the multiplication table of a number n.
i=1
while i<=10:
    print(2*i)
    i+=1
#wap to print the elements of the following list using a loop
nums = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
idx  = 0
while idx < len(nums):
    print(nums[idx])
    idx  += 1
#wap to search for a number x in this tuple using loop (1,4,9,16,25,36,49,64,81,100)
tup = (1,4,9,16,25,36,49,64,81,100)
x =49
i =0
while i< len(tup):
    if (tup[i]==x):
        print("found :",i)
        break
    else:
        print("finding")    
    i+=1
#wap to break loop
i=0
while i<=5:
    print("afzal")
    if (i==3):
        break
    i+=1
#wap 2nd program of break loop
tup2 = (1,2,3,4,5,6,7,8,9,10)
x=7 
i=0
while i<len(tup2):
    if(tup2[i]==x):
        print("found :",i)
        break
    else:
       print("finding:")
        
    i+=1  
print("end of loop")    
#wap to continue loop 
i = 0
while i<5:
    if (i==3):
        i+=1
        continue
    print(i)
    i+=1
#for loop(we are using for loop for sequence type of data)
list = [1,2,"afzal",45,67,"murtaza"]
for el in list:
    print(el)
 
print("END")
#using break condition in for loop
list2=[1,2,3,4,5,6,7,8,9]
for el2 in list2:
    if(el2==7):
        print("found:",el2)
        break
    else:
        print(el2)
print("END")
#practice questions for loop
#wap to print the elements of the following list using a loop:[1,4,9,16,25,36,49,64,81,100]
qs1 = [1,4,9,16,25,36,49,64,81,100]
for elqs1 in qs1:
    print(elqs1)
print("END")  
#wap to search for a number x in tuple using loop:(1,4,9,16,25,36,49,64,81,100)
#through my thinking
qs2 =(1,4,9,16,25,36,49,64,81,100)
for elqs2 in qs2:
    if(elqs2==49):
        print("found:",elqs2)
        break   
    else:
        print("finding")
#through lectature
qs2t =(1,4,9,16,25,36,49,64,81,100)
x=49
ind =0
for elqs2t in qs2t:
    if(elqs2t==x):
        print("found:",ind)
        break
    ind+=1  
print("END") 
#range in for loop
for a in range(10):
    print(a) 
print("END")  
#2nd condition
for a2 in range(2,100):#range(start,stop)
    print(a2)
print("END")    
#3rd condition
for a3 in range(2,100,2):#range (start,stop,step) using print even or odd numbers
    print(a3)
#3rd condition
for a4 in range(1,100,2):#range (start,stop,step) using print even or odd numbers
    print(a4)
#practice question of range
#wap to print numbers from 1 to 100.
for r1 in range(1,101):
    print(r1)
#wap to print numbers from 100 to 1.
for r2 in range(100,0,-1):
    print(r2)    
#wap to print multiplication table of a number n
for r3 in range(6,61,6) :
    print(r3)   
# #input number n from user
n=int(input("enter number:"))
for t in range(n,n*11,n):
    print(t)
#pass statement
for a in range(100):
    pass #pass is pause the last condition
print("afzal")
#wap to find the sum of first n numbers.(using while loop)
num =int(input("enter num:"))
sum =0
i = 1
while i<=num:
    sum+=i
    i+=1
print("total number of sum",sum)
#wap to find the factorial of first n numbers .(using for loop)
n = int(input("enter n:"))
fact =1
for mul in range (1,n+1):
    fact*=mul
print(fact)