#10. Write a Python program to convert a string to a list. 
string=input("enter a string\t:")
#.for conversion of a string to a list split() has to be used.
string_list=string.split()#.by default,split() has space as a seperator
print("after conversion:-",string_list,"is of type:-",end="")
print(type(string_list))
