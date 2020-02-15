user = int(input())
output = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

for i in range(1, user + 1, 1):
    im = str(i)

    for x in range(len(im)):
        output[int(im[x])] += 1

for i in range(0, 10, 1):
    print(i, " ", output[i])