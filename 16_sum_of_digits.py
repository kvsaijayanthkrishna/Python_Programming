#16. Write a Python program to compute sum of digits of a given string. 
number=input("enter a number\t:")
total=0
for a in number:
    total+=int(a)
print("sum of digits of {0} is {1}".format(number,total))
