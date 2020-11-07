#case reverse of an alphabet
ch=input("enter a character\t:")
print("Input:-",ch)
if(65 <= ord(ch) <= 90):ch=ord(ch)+32
elif(97 <= ord(ch) <= 122):ch=ord(ch)-32
print("Output:-",chr(ch))
