#types of string
#str
str="my name is afzal"
print(str)
#concentation str
str1="my name is "
str2="afzal"
sum=str1+str2
print(sum)
#length of string
name="afzal"
len=len(name)
print("len:",len)
#indexing of str
ind=name[0]
print(ind)
#slicing of string
sli=name[0:]
print(sli)
#slicing negative indexing
neg=name[-1:-5]
print(neg)
#string functions 
#endswith string
str="my name is afzal"
print(str.endswith("afzal"))
print(str.endswith("my"))
#capitalize string
str="i am a ai ml engeener"
print(str.capitalize())
#replace string
str="cheetah hi kehde "
print(str.replace("cheetah","sher"))
#find string
str="go and take action"
print(str.find("take"))
#count string (occurance string)
str="its okay i will do my best again"
print(str.count("i"))
#practice questions
#wap to input user's first name and print its lenth
username1=input("user name:")
print(username1,"murtaza")
len=len(username1)
print (len)
#wap to find the occurance of '$' in a string
str="i make in $ i earn 1000$ per month"
print(str.count("$"))
