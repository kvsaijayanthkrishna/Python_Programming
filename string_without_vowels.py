#lec-18/slide-19
#Write a program to accept a string from the user and display it vertically
#but don’t display the vowels in it using while loop.
string=input("enter a string\t:-")
length=len(string)
i=0
while i<length:
    if (string[i]=='a')or(string[i]=='e')or(string[i]=='i')or(string[i]=='o')or(string[i]=='u'):
        i=i+1
        continue
    print(string[i])
    i=i+1
print()
