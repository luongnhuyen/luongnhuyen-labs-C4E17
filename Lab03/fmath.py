from random import *
import eval

x = randint(0,10)
op = choice(['+','-','*','/'])
y = randint(0,10)

result = 0

result = eval.calc(x,y,op)

error = choice([-1,0,0,0,0,-1])

display_res = result + error

print("{0} {1} {2} = {3}".format(x,op,y,display_res))

answer = input("Y/N: ").upper()

if error == 0:
    if answer == "Y":
        print("Dung")
    elif answer == "N":
        print("Sai")
else:
    if answer == "Y":
        print("Sai")
    elif answer == "N":
        print("Dung")
