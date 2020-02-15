import random

pt = random.sample(range(1, 10), 3)
print(pt)

answer = 0
countt = 0

while(answer == 0):
    print("입력 ")
    user = str(input())

    if(len(user) != 3):
        print("입력 오류")
        countt = countt + 1
        continue

    strike = 0
    ball = 0

    for x in range(0, 3, 1):
        for y in range(0, 3, 1):
            if str(pt[x]) == str(user[y]) and x == y:
                strike = strike + 1
            elif str(pt[x]) == str(user[y]) and x != y:
                ball = ball + 1

    print(strike, "strike")
    print(ball, "ball")

    if strike == 3:
        answer = 1
    else:
        countt = countt + 1

print(countt, "번 만에 성공하셨습니다!")