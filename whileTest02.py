i = 1
while(i<=9):
    j = 1
    while(j<=i):
        # print(i,"*",j,"=",i*j,end="\t")
        print(f"{i}*{j} = {i*j}",end="\t")
        j += 1
    print()
    i+=1
