name=input("Enter your name ")
print("Welcome",name,"to the game")

answer=input("S for Start/Q for Quit ").lower()
if answer=="s":
    answer=input("Straight/Left/Right ")
    if answer=="Straight":
        print("adios")
    if answer == "Left":
        answer=input("Go back/continue ")
        if answer=="Go back":
            print("Stay back")
        else:
            print("Go ahead")
            answer=input("Now Stop/Continue ")
            if answer=="Stop":
                print("Good choice")
            else:
                print("BAD")
    if answer == "Right":
        print("nothing left")
else:
    quit()
