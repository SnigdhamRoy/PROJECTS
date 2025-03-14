import random
user_score=0
computer_score=0
options=['rock','paper','scissors']

while True:
    user=input("TYPE rock,paper,scissor or q for quit ")
    if user=='q':
        quit()
    if user not in options:
        continue
    r=random.randint(0,2)
    comp = options[r]
    print("Computer picked->",comp)
    if user=='rock' and comp=='scissor':
        print('You won')
        user_score+=1
        break
    elif user == 'paper' and comp == 'rock':
        print('You won')
        user_score += 1
        break
    elif user=='scissor' and comp=='paper':
        print('You won')
        user_score += 1
        break
    else:
        print('Lost!')
        computer_score+=1

print("User score ", user_score)
print("COmp score ", computer_score)