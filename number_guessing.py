import random
t=input("Enter a number = ")
if t.isdigit():
    t = int(t)
    if t<=0:
        print("Must be LArger than 0")
        quit()
else:
    print("Type a number")
    quit()
r=random.randrange(0,t)
g=0
while True:
    g+=1
    user = input("Enter your choice ")
    if user.isdigit():
        user=int(user)
    else:
        print("Type a number")
        continue
    if user==t:
        print("Good")
        break
    else:
        print("Bad")
print("No of guesses ",g)


