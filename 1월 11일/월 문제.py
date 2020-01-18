year = int(input())
month = int(input())

if month == 2:
    if year % 4 == 0:
        print("29일")
    else:
        print("28일")
elif(month == 4 or month == 6 or  month == 9 or month == 11):
    print("30일")
else:
    print("31일")