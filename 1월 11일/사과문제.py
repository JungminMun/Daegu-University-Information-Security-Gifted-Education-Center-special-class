apple = input()
applemoney = int(input())

if apple == "신선":
    if applemoney >= 2000:
        print("안삼")
    if applemoney >= 1000:
        print("5")
    else:
        print("10")
else:
    print("안삼")  