
n=eval(input("how many employes?\t:"))
print("enter employee details (idno name salary role city)")
emps=list()
for p in range(n):
    details=list()
    details=[eval(x) if(x.isnumeric()) else x for x in input(f"enter employee {p+1} details").split()]
    emps.append(details)
for p in emps:print(p)
#Removing particular field. here we are removing city details.
print("After removing city")
for p in emps:p.pop(4)
for p in emps:print(p)
