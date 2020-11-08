#Write a program to accept an alphanumeric string from the user.
#Now extract only digits from the given input and add it to the list.
#Finally print the list.
#Make sure your list contains numeric representation of digits
string=input("enter an alphanumeric string\t:")
num_list=list()
for i in string:
    if 48<=ord(i)<=57:
        num_list.append(int(i))
print("numbers present in above string =",num_list)
