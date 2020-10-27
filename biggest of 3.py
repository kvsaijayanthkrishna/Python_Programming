#. WAP to accept three nos from the user and print greatest of three numbers
a,b,c=(input("enter three numbers (sep by ,)\t:")).split(",")
if a>b:
    if a>c:print(a,"is big")
    else  :print(c,"is big")
else:
    if b>c:print(b,"is big")
    else  :print(c,"is big")
