#2. Write a Python program to count the number of characters (character frequency) in a string.  
#Sample String : google.com'
#Expected Result : {'o': 3, 'g': 2, '.': 1, 'e': 1, 'l': 1, 'm': 1, 'c': 1}
string=input("enter a string\t:")
letter=""
print("output:-")
for s in string:
    if s not in letter:
        print("['{0}': {1}]".format(s,string.count(s)),end=", ")
    letter+=s
print()
