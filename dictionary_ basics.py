#dictionary in python
dict ={
    "name":"afzal",
    "age":21,
    "marks":[23,23,23,23,23],#we  can also create a list in dict
    "sbjt":("dbms","computer sceince","bca","b.tech",)#we can also create tuples in dict
}
print(dict)
print(len(dict))#we can find the lenth in dict
print(type(dict))#we can print the type if dict
print(list(dict))# we can make list of dict
print(tuple(dict))#we can create tuple of dict
# create dict in dict we can create dict in dict
dict2={
    "name2":"amjad",
    "age2":19,
    "subjest and marks":{
        "phy":23,
        "chem":40,
        "bio":59.9 
    }
}
print(dict2)
#dict methods
print(dict2.values())#we can also access value of keys in dict
print(dict2["age2"]) #we can also access the value of word in dict
print(dict2.get("name2"))#we have two method os access the value in dict
print(dict2.keys())#we can also access the keys in dict
print(dict2.items())#we can also convert dict in to tuple
update = {
    "name3":"abdul",
    "age3":23,
    }
print(dict2.update(update))#we can also add more dict in dict and update
print(update)
print(dict2)
#we can also create empty dict after add the values
dict3 = {} # syntax of empty dict
update2= {"afzal":23,}
print(dict3.update(update2))
print(dict3)
#practice questions
"""store following word meaning in a python dict:
table:a peice of furnitur,list of facts and figurs
cat:a small animal"""
qst1 ={
    "table":("a piece of furniture","list of facts and figures"),
    "cat":"a small animal"
}
print(qst1) 
"""wap to enter marks of 3 subjects from the user and store them in a dictionary.
start with an empty dictionary and add one by one. use subject name as key and marks as value."""
qst2 = {}
chem = {"chem":int(input("enter chem marks:"))}
bio = {"bio":int(input("enter bio marks:"))}
phy = {"phy":int(input("enter phy marks:"))}
qst2.update(chem)
qst2.update(bio)
qst2.update(phy)
print(qst2)
#2nd formate
dict={}
dict.update({"chem":int(input("enter marks of chem:"))})
dict.update({"bio":int(input("enter bio marks:"))})
dict.update({"phy":int(input("enter phy marks:"))})
print(dict)
