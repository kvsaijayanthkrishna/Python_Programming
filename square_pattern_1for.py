m=int(input("enter rows\t:"))
n=int(input("enter coloumns\t:"))
for i in range(1,m*n+1):
    print("*",end=" ")
    if(i%m==0):
        print()
