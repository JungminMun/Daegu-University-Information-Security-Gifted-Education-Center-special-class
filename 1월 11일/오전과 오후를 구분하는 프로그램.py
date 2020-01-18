import datetime

now = datetime.datetime.now()

if now.hour < 12:
    print("현재 시간은" ,now.hour, "시로 오전 입니다.")

if now.hour >= 12:
    print("현재 시간은" ,now.hour, "시로 오후 입니다.")