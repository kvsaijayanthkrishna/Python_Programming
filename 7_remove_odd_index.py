#7. Write a Python program to remove the characters
#which have odd index values of a given string.
string=input("enter a string\t:")
new_string=""
i=0
for s in string:
    if(i%2==0):
       new_string+=s
    i=i+1
print("new string:-",new_string)
