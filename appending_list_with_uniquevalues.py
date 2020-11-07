#Write a program to accept 5 unique integers from the user.
#Make sure if the integer being entered is already present in the list
#your code displays the message “Item already present” and
#ask the user to reenter the integer.
mylist=list()
i=1
while i<=5 :
    n=int(input(f"enter {i} integer\t:"))
    if n in mylist:
        print("Item already present")
        continue
    mylist.append(n)
    i=i+1
print("Integers entered by the user are:")
for i in mylist:print(i)
