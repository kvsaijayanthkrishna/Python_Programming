#Write a program to accept 2 lists from the user of 5 nos each.
#Assume each list will have unique nos. Now find out how many items
#in these lists are common .
list1=list()
list2=list()
print("enter elements for list1:-")
i=1
while i<=5 :
    n=int(input(f"enter {i} integer\t:"))
    if n in list1:
        print("Item already present")
        continue
    list1.append(n)
    i+=1
print()
print("enter elements for list2:-")
i=1
while i<=5 :
    n=int(input(f"enter {i} integer\t:"))
    if n in list2:
        print("Item already present")
        continue
    list2.append(n)
    i+=1
print()
common=0
for i in list1:
    if i in list2:
        common+=1
print(f"{common} elements are in common")
