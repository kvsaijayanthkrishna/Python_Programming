n=int(input("enter a number\t:"))
fact=1
for i in range(1,n+1):
    fact*=i
print("factorial of {0} is {1}".format(n,fact))
