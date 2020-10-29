#13. Write a Python program to move spaces to the front of a given string.
string=input("enter a string\t:")
string_list=string.split()
length=len(string_list)
new_string=""

for string in string_list[1: ]:
    new_string+=" "
for string in string_list:
    new_string+=string
print("after removing spaces\t:-",new_string,sep="")
