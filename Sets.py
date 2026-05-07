#sets in python
collection = {1,2,3,"afzal,","murtaza"}
print(collection)
#we can only store unique value in sets
collection1 = {1,2,3,4,4,4,5,5,6,6,}#we can only store the value is unique and set is return output is only unique 
print(collection1)
print(len(collection1))#we can also print the length of collecyion
print(type(collection1))#we can also prinnt the type of sets
#create empty set
collection3 = set() #syntax of empty sets
#methods of sets
collection3.add("afzal")#we can add the value in in sets 
collection3.add(1)
collection3.add(1)
collection3.add(4)
print(collection3)
collection3.remove(4)#we can also remove the value in sets
collection3.remove("afzal")
print(collection3)
collection3.pop()# we can print random value in sets
print(collection3)
collection3.clear()# we can clear all value of set in sets
print(len(collection3))
# we can add two sets in one sets
set1 = {1,2,3,4,5,6,7}
set2 = {8,9,10}
print(set1.union(set2))
#we can print combine value of two sets
set3 = {1,2,3,4,}
set4 ={4,3,55,6}
print(set3.intersection(set4))
#practice question
"""you are given a list of subjects for students.assume one classroom is required for 1 subject.how many classroom are needed by all students
python java c++ python javascript java python java c++ c"""
qst1 = {"python","java","c++","python","javascript","java","python","java","c++","c"}
print(len(qst1))
print(qst1)
#figure out a way to store 9 and 9.0 as separate value in the set(you can take help of built-data types)
qst2 = {9,9.0}
print(qst2)
#2nd possible solution
value ={
    ("float",9.0),
    ("int",9)
}
print(value)