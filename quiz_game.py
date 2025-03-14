print("Welcome to quiz")

x=input("Do you want to play?  ")
if x.lower()== "no":
    exit("Ok")
else:
    print(" Alright! ")
score=0
a=input("Do yo know your name? ")
if a.lower()=="yes":
    print("Good")
    score+=1
else:
    print("Wrong")
a=input("What is Cpu? ")
if a.lower()=="central Processing Unit":
    print("Good")
    score+=1
else:
    print("Wrong")
a=input("What is Gpu? ")
if a.lower()=="graphical processing unit":
    print("Good")
    score+=1
else:
    print("Wrong")

print("You got " + str(score) +" correct")
print("Percentage "+str((score/3)*100)+"%")



