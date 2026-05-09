#del keyword(del keyword is delete the class)
class car:
    def __init__(self,name):
        self.name=name
ca1=car("fortuner")
print(ca1.name) 
del ca1.name # this a syntax of del a class we are using for delete class
print(ca1.name)       
#private attributes and methods (we can private the attribute in class for security after that we are only access the attr in class not outside the class)
class car:
    def __init__(self,name,color):
        self.name=name
        self.__color=color #(the __ is represt the attrr is pvt in class and we can pvt the class this type)
    def color(self ):
        print(self.__color) #(we are create another func for access the pvt method or class and attrr)    
c1=car("fortuner","black")
print(c1.name)
c1.color()    
#inheritance /we can inherit the class and attr from parent class to child class(3 types of inheritance)
#single inheritance
class car1:
    def start(self):
        print("car started.....!!")
    def stop(self):
        print("car stoped...!!")
class toyota(car1): #we can inherit the class by using(car1) syntax
    def __init__(self,name,brand):
        self.name=name
        self.brand=brand
t1=toyota("fortuner","toyota")
print(t1.brand)  
print(t1.name)
t1.start()
t1.stop()# we can see the attrr of car1 class has been access in 2nd class toyota
#multi-level inheritance(when we are inherit the child class into a child class)
class car2:
    def start(self):
        print("car started....!!!")
    def stop(self):
        print("car stopedd...!!")
class brand(car2):
    def brand(self):
        print("toyota")       
class fortuner(brand):
    def __init__(self,name,color,model):
        self.name=name
        self.color=color
        self.model=model
for1=fortuner("fortuner","black","2025")
for1.brand()           
print(for1.name)
print(for1.color)
print(for1.model)
for1.start()
for1.stop()          
#multiple inheritance (in this inheritace we have two parent and one child)
class car3:
    def start(self):
        print("car started..!!!!")
    def stop(self):
        print("car stoped.....!!!!")
class brand1:
    def brand(self):
        print("toyota")  
class fortuner1(car3,brand1): #we are inherit the two parents class in one child class
    def __init__(self,name,color,model):
        self.name=name
        self.color=color
        self.model=model
for2=fortuner1("fortuner","black",2025)
for2.brand()
print(for2.name)
print(for2.color)
print(for2.model)
for2.start()
for2.stop()
#super method(the using of super method we can access the constructor of class)
class car4:
    def __init__(self,start,stop):
        self.start=start
        self.stop=stop
class car5(car4): # if we are use super we need also inheritance the class is must
    def __init__(self,name,brand,start,stop):
        super().__init__(start,stop)#syntax of super method()
        self.name=name
        self.brand=brand
ca3=car5("fortuner","toyota","car started...!!","car stoped...!!")
print(ca3.brand)
print(ca3.name)
print(ca3.start)
print(ca3.stop) 
#class method decorator (we can change the value of class attrr by classmethod)
class A:
    name="amjad"
    def __init__(self,name):
        @classmethod
        def changeName(cls,name): #syhtax os classmethod
          cls.name=name
a1=A("afzal")
print(a1.name)        
#property decorator (we are use property decorator on any method in the class to  use the method as a property)
class student:
    def __init__(self,chem,bio,phy):
        self.chem=chem
        self.bio=bio
        self.phy=phy    
    @property #the syntax of property method
    def percentage(self):
        return str((self.chem+self.bio+self.phy)/3)+"%"
stu1=student(98,97,95)
print(stu1.percentage)
stu1.chem=90
print(stu1.percentage)
stu1.bio=80
print(stu1.percentage)
#polymorphism(operator overloading)
class complex:
    def __init__(self,real,img):
        self.real=real
        self.img=img
    def Shownum(self):
        print(self.real,"i","+",self.img,"j")
    def __add__(self,com2):    
        Numreal=self.real+com2.real
        Numimg=self.img+com2.img
        return complex(Numreal,Numimg)   
    def __sub__(self,com2):    
        Numreal=self.real-com2.real
        Numimg=self.img-com2.img
        return complex(Numreal,Numimg)  
com1=complex(1,4)
print(com1.Shownum()) 
com2=complex(2,4)
print(com2.Shownum()) 
com3=com1+com2
print(com3.Shownum())  
com4=com1-com2
print(com4.Shownum())   
#practice questions
#qs1
class circle:
    def __init__(self,r):
        self.r=r
    def area(self):
        return (22/7)*self.r**2
    def perameter(self):
        return 2*(22/7)*self.r

c1=circle(21)  
print(c1.area())
print(c1.perameter())      
#qs2
class emply:
    def __init__(self,role,dept,salary):
        self.role=role
        self.dept=dept
        self.salary=salary
    def Showdetails(self):
        print("role=",self.role,"\ndept=",self.dept,"\nsalary=",self.salary) 
class engeener(emply):
    def __init__(self,name,age):
        self.name=name
        self.age=age
        super().__init__("enginer","it",60000)         
engg1=engeener("afzal","21")
print(engg1.Showdetails())          
#qs3
class order:
    def __init__(self,item,price):
        self.item=item
        self.price=price
    def __gt__(self,ordr2):
        return self.price >ordr2.price    
odr1=order("coffee",100)
odr2=order("pizza",500)
print(odr1>odr2)        


