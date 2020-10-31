#Write a function called absolute() to accept an integer as argument and
#return it’s absolute value. Finally call it to get the absolute value of -7 and 9
def absolute(n):
    if n>0:
        return n
    else:
        return -n
n=int(input("enter any integer\t:"))
print("absolute value of {0} is {1}".format(n,absolute(n)))
