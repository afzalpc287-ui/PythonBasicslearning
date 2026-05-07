#files 
#file read
f=open("demo.text","r")
data= f.read()#we  can also define parameter in()
print(data)
print(type(data))
line1=f.readline()
line2=f.readline()
line3=f.readline()
print(line1)
print(line2)
print(line3)
f.close()
#writing file
f2 = open("demo.text","w")
f2.write("my name is afzal\n")
f.close()
#append in file
f3 = open("demo.text","a")
f3.write("father name is murtaza")
f.close()
# combine file action
f4 = open("demo.text","r+")
f4.write("hello guys")
#another type of  syntax of writing a file
with open("demo.text","w") as f6:
    data2 = f6.write("new data")
    print(data2)
with open("demo.text","r") as f5:
    data =f5.read()
    print(data)
#writing file
#delete a file'
import os
os.remove("demo.text")
#practice qs
"""create a new file "practical.txt" using python. add the following data in it:
hi everyone
we are learning file i/o
using java
i like programming in java"""
with open("practice.txt","w")as file:
    file.write("hi everyone\nwe are learning file i/o\ousing java\oi like programming language")
#qs2
with open("demo.text","r") as f6:
    data = f6.read()
    new_data=data.replace("afzal","amjad")
    print(new_data)
with open("demo.text","w") as f:
    f.write(new_data)
#qs3     
with open("demo.text","r") as f:
    data = f.read()
    if(data.find("amjad")!=1):
        print("found")
    else:
        print("not found")
#qs4
def check_forline():
    word ="amjad"
    data =True
    line_no =1
    with open("demo.text","r")as f:
        while data:
            data = f.readline()
            if(word in data):
                print(line_no)
                return
            line_no +=1   
    return -1         

check_forline()
#qs5
count=1
with open("demo.text","r") as f:
    data =f.read()
    print(data)
    nums=data.split(",")
    for val in nums:
        if(int(val)%2==0):
            count +=1
print(count)