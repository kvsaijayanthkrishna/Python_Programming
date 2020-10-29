#12.Write a Python program to remove spaces from a given string. 
string=input("enter a string\t:")
string_list=string.split()
length=len(string_list)
new_string=""
for string in string_list:
    new_string+=string
print("after removing spaces\t:-",new_string)
