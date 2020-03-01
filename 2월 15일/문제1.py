countt = 0 
for i in range(0, 10001, 1): 
    istring = str(i) 

    for y in range(len(istring)): 
        if(istring[y] == "8"): 
            countt = countt + 1 
            break 

print(countt) 