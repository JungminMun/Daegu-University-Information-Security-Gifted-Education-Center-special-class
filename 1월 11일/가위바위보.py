import random

number = random.randint(0,2)
user = input()

if(number == 0):
    print("묵")
elif(number == 1):
    print("찌")
else:
    print("빠")
if(number == 0 and user == "빠" or number == 1 and user == "묵" or number == 2 and user == "찌"):
    print("이김")
elif(number == 0 and user == "찌" or number == 1 and user == "빠" or number == 2 and user == "묵"):
    print("비김")
else:
    print("짐")