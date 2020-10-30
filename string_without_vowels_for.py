#lec-19/slide-8
#Write a program to accept a string from the user and display it vertically
#but don’t display the vowels in it using for loop.
string=input("enter a string\t:-")
for ch in string:
    if ch in "aeiou":
        continue
    print(ch)
print()
