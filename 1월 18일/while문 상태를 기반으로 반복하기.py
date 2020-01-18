test = [1, 2, 2, 2]
value = 2


for i in range(len(test)):
    if(value in test):
        test.remove(value)

print(test)