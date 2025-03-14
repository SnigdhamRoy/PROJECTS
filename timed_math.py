import random
import time

operator=['+','-','*']
min_operand=3
max_operand=10
total=5

def calc():
    left=random.randint(min_operand,max_operand)
    right=random.randint(min_operand,max_operand)
    o=random.choice(operator)
    x=str(left)+" "+ o +" "+str(right)
    answer=eval(x)
    return x,answer

start=time.time()
for i in range(total):
    q,a=calc()
    while True:
        guess=input("Problem #" + str(i+1) + ": "+ q + " = ")
        if guess==str(a):
            break
end=time.time()
total_time=end-start

print("Total time taken: ",total_time)
print("------------------------------------------")