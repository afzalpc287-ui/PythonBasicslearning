#tuples in python
tub=(1,2,3,4,5,5,5,5,5)# tuples written method
print(tub)
#we can print len and type in tuple
print(type(tub))
print(len(tub))
#we can do slicing in tuples
print(tub[2:4])
#we can find the element in tuples
print(tub.index(3))
#we can count the elements in tuples
print(tub.count(5))
#tuple is totally like that string
#wap to count the number of student with the""A" grade in the following tuple
student =("A","C","A","D","A","B","A","C","A","B")
print(student.count("A"))
print(student)
# store the above values in a list and sort them from A to D
# through my understanding
val = []
val.append(input("enter first value:"))
val.append(input("enter 2nd value:"))
val.append(input("enter 3rd value:"))
val.append(input("enter 4th value:"))
val.sort()
print(val)
