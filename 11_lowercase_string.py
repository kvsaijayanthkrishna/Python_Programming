#.11. Write a Python program to lowercase first n characters in a string.
string=input("enter a string\t:-")
n=int(input("enter n(for lowercase of first n characters)\t:-"))
new_string=((string[0:n]).lower())+string[n: ]
print("after lowercase of first n characters the string is\n",new_string,sep="")
