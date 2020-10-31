#Write a function called factorial() which accepts a number as argument and
#returns it’s factorial. Finally call the function to calculate and
#return the factorial of the number given by the user.
def factorial(n):
    fact=1
    for i in range(1,n+1):
        fact*=i
    return fact
n=int(input("enter any number\t:"))
print("factorial of {0} is {1}".format(n,factorial(n)))
