#15. Write a Python program to capitalize
#first and last letters of each word of a given string.
string=input("enter a string\t:")
string_list=string.split()
length=0
new_string=""
for string in string_list:
    length=len(string)
    if(length==1):
        new_string+=((string[0]).upper()+" ")
    else:
        new_string+=((string[0]).upper()+string[1:length-1]+(string[-1]).upper()+" ")
print("output:-",new_string)
