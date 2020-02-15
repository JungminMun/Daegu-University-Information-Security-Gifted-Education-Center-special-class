countt = 0 #카운트를 저장하는 정수형 변수
for i in range(0, 10001, 1): #for문을 0부터 10000까지 범위 지정
    istring = str(i) #istring변수는, 정수형 i를 문자열으로 변환한 변수입니다.

    for y in range(len(istring)): #for문은 istring변수의 길이까지 범위를 지정
        if(istring[y] == "8"): #만약에 istring변수에 8이 있다면
            countt = countt + 1 #카운트를 더해줍니다
            break #첫번째 문제는 8이 들어간 숫자가 몇개인지 알려주는 거니까, 조건식에 맞다면 for문을 끝냅니다

print(countt) #countt 변수를 출력합니다

print("인생이 시발 좇같네")
print("인생은 현실이다")