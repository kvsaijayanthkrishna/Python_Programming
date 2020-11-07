#Write a program to accept 5 integers from the user and store them in a list
#display these integers in the form of a list and also vertically
#also, display their sum.
mylist=list()
i=1
n=0
while i<=5:
    n=int(input(f"enter {i} element:"))
    mylist.append(n)
    i=i+1
print(mylist)
for i in mylist:print(i)
print("Sum =",sum(mylist))

