number = float(input())

if number == 0:
    print("시대를 앞서가는 혁명의 씨앗")

elif 0 < number < 0.5:
    print("플랑크톤")

elif 0.5 <= number <  1:
    print("자벌레")

elif 1 <= number < 1.75:
    print("불가촉천민")

elif 1.75 <= number < 2.3:
    print("오락문화의 선구자")

elif 2.3 <= number < 2.8:
    print("일탈을 꿈꾸는 소시민")

elif 2.8 <= number < 3.5:
    print("일반인")

elif 3.5 <= number < 4.2:
    print("현 체제의 수호자")

elif 4.2 <= number < 4.5:
    print("교수님의 사랑")

elif number == 4.5:
    print("신")

else:
    print("입력 오류")