#pro.1 guess right number
# # by me by the help of gemini
import random
user_key=int(input("guess no"))
ra=random.randint(1,100)
print("the random no is:",ra)
if(user_key>ra):
    print("you guess bigeer try again")
elif(user_key==ra):
    print("you win")    
else:
    print("you guess smaller try again")  
#by lecturare
import random
target=random.randint(1,100)
while True:
    userchoice=(input("GUESS NUMBER OR QUIT(Q):"))
    if(userchoice=="Q"):
        break
    userchoice=int(userchoice)
    if(userchoice==target):
        print("----YOU WIN----")
        break
    elif(userchoice>target):
        print("YOU GUESS BIGGER")
    else:
        print("YOU GUESS SMALLER")
print("----GAME OVER-----") 
#pro.2 random password generator
import random
import string
pass_len=int(input("enter len of pass you want:"))
char_value=string.ascii_letters + string.digits + string.punctuation
#list comprehention 
password ="".join([random.choice(char_value)for i in range(pass_len)])



for i in range(pass_len):
    password+=random.choice(char_value)
print("your generated password is:",password)    
#purposal project
print("-----I LOVE YOU-----")
choose_option=input("choose option(yes or no):")
if(choose_option=="yes"):
    print("congrates lets go on date")
elif(choose_option=="no"):
    print("its okay")
else:
    ("giue answer in just two option yes or no")    
print("lets meet later bye")    
