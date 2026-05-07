#list in python
marks = [90,89,78,80,78] #sytax of list
print(marks)
diff = ['afzal',21,'delhi']
print(diff)
#indexing in list
diff[0]='amjad'
print(diff)
print(len(diff))
print(type(marks))
#list slicing
print(marks[1:3])
print(marks[-4:-1])
#list methods
#we can add the value in list
job=[1,2,3]
print(job.append(4))
print(job)
#we can manage the list in accending order
print(job.sort())
print(job)
#we can manage the list in decending order
print(job.sort(reverse=True))
print(job)
#we can reverse the list
print(job.reverse())
print(job)
#we can remove the first 0ccurence from list
print(job.remove(2))
print(job)
#we can insert the value in list
print(job.insert(2,5))
print(job)
# we can remove the value from list
print(job.pop(2))
print(job)
#wap to ask the user to enter names of their 3 fav movie and store them in a list
movie1 = input("enter 1st movie:")
movie2 = input("enter 2nd movie:")
movie3 = input("enter 3rd movie:")
list = [movie1,movie2,movie3]
print(list)
print(type(list))
#same q/a from lectarure
movies = []
movies.append(input("write first movie:"))
movies.append(input("write 2nd movie:"))
movies.append(input("write 3rs movie:"))
print(movies)
print(type(movies))
#wap to check if a list contains a palindrom of elements 
list1 = [1,2,3,2,1]
list1_copy=list1.copy()
list1.reverse()
if(list1==list1_copy):
    print("palindrom")
else:
    print("not palindrom")    
