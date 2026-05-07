#oops part 1(object oreinted programming)
#how to create class and in object
class Student:
    name="AFZAL"
s1=Student()
print(s1.name)    
class car:
    name ="M4"
    colour="BLACK"
    brand = "BMW"
car1 =car()
print(car1.name)
print(car1.colour)
print(car1.brand)    
# in_it function as also called constructor(when we are create object by using class the in_it function is automatic call in program)
class third:
    def __init__(self,fullname):
        self.name=fullname
        self.fav=fullname
        print("adding the object in class by in it function:")
one =third("afzal") # we can also adding the objects by help of in it function
print(one.name)        
two  =third("AMJAD")
print(two.name)
three =third("BMW")
print(three.fav)
#another type of constructer def
class two:
    # default constructor
    def __init__(self):
        pass
    #parameter constructor
    def __init__(self,name,marks,sec):
        self.name=name
        self.marks=marks
        self.sec=sec
first=two("afzal",95,"A")
second=two("amjad",90,"B")
print(first.name,first.marks,first.sec)
print(second.name,second.marks,second.sec)
#class and instance attributes
class one:
    college="abc college"#class attr
    def __init__(self,name,sec,marks):
        self.name=name#this is object attr also called instance atrr
        self.sec=sec#and always object attr have higher priority
        self.marks=marks#then class atrr(class str<object atr)
o1= one("afzal","A",90)
o2= one("ammjad","A",90)
print(o1.name,o1.sec,o1.marks,one.college)#the one.college is a class attr we dont need dto def
print(o2.name,o2.sec,o2.marks,one.college)#again and again this is common value usable  
#methods is as function we are using in list and others
class o1:
    def __init__(self,name,subject,sec):
        self.name=name
        self.sub=subject
        self.sec=sec
    def welcome(self): # so this is a method we can add in class after constructor
        print("welcome",self.name,) # ("parametr",we can also call atrr for constructor)
    def subject(self):
        return self.sub        
o11=o1("afzal","chem","A")
o11.welcome()
print(o11.subject())
#practice question
#qs1
class qs1:
    def __init__(self,name,smarks1,smarks2,smarks3):
        self.name=name
        self.smarks1=smarks1
        self.smarks2=smarks2
        self.smarks3=smarks3
    def avg(self):
        sum=self.smarks1+self.smarks2+self.smarks3
        print("the avg of your marks",sum/3)    
qs11=qs1("afzal",90,40,54)        
print(qs11.name,qs11.smarks1,qs11.smarks2,qs11.smarks3)
qs11.avg()
#by lectarure
class qs12:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    def sum(self):
        sum=0
        for val in self.marks:
            sum+=val
        print("hi",self.name,"avg of yours marks is",sum/3)

qs121=qs12("afzal",[90,40,54]) 
qs121.sum()
#static method decorator
class stu1:
    @staticmethod #this is static method we dont need self write in it and we are using in only class 
    def college():
        print("ABC college")
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    def sum(self):
        sum=0
        for val in self.marks:
            sum += val
        print("hi",self.name,"sum of your marks:",sum)
stu11=stu1("afzal",[90,20,30])
stu11.sum()
stu1.college()
#abstraction (when we are hide the unnecessary details and showing essential feature)
class car:
    def __init__(self):
        self.acc=False
        self.brk=False
        self.clutch=False
    def started(self):
        self.acc=True
        self.clutch=True
        print("car started")
car1=car()
car1.started()           
#encapsulation(when we are store the data and function in single one object is called encapsulation)
#practice question
#qs1
class account:
    def __init__(self,bal,acc):
        self.balance=bal
        self.account_no=acc
    def debit(self,amount):
        self.balance-=amount
        print("Rs.",amount,"\ndebit from your acc:",self.account_no,"\nthe total balance is:",self.get_balance())
    def credit(self,amount):
        self.balance+=amount
        print("Rs.",amount,"\nhas been credit in acc:",self.account_no,"\nthe total balance is:",self.get_balance())   
    def get_balance(self):
        return self.balance         
ac1=account(10000,12345678)
ac1.debit(500)
ac1.credit(5000)
ac1.debit(6000)
ac1.credit(5600)


