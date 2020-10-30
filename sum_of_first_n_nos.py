#sum of first n numbers
n=int(input("enter a number\t:"))
sum=0
for i in range(1,n+1):
    sum+=i
print("sum of {0} numbers is {1}".format(n,sum))
