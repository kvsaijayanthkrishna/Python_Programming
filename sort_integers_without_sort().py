#Write a program to accept any n random integers from the user
#and add them in a list in such a way that list always remains sorted.
#DO NOT USE THE FUNCTION sort()
sort_list=list()
n=int(input("how many numbers do u want to enter\t:"))
count=0
i=1
while i<=n:
    count=0
    num=int(input(f"enter {i} integer\t:"))
    for j in sort_list:
        if num<j:
            break
        count+=1
    sort_list.insert(count,num)
    i+=1
print("sorted list =",sort_list)

