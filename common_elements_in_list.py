#Assume each list will have unique nos Now find out how many items
#in these lists are common and print those common elements.
list1=list()
list2=list()
print("enter list1 elements:-")
i=1
while i<=5:
    n=int(input(f"enter {i} element\t:"))
    if n in list1:
        print("Item already present")
        continue
    list1.append(n)
    i+=1
print()
print("enter list2 elements:-")
i=1
while i<=5:
    n=int(input(f"enter {i} element\t:"))
    if n in list2:
        print("Item alread present")
        continue
    list2.append(n)
    i+=1
print()
common_list=list()
common=0
for i in list1:
    if i in list2:
        common_list.append(i)
        common+=1
print(f"{common} elements are in common")
print("common elements are",end=" ")
for i in common_list:print(i,end=" ")
print()
 
