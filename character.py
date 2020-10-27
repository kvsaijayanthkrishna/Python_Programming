#. Wap to input a character and print whether it is capital or small or digit or a symbol.
ch=input("enter a character\t:")
if 65<=ord(ch)<=90:print(ch,"is capital letter")
elif 97<=ord(ch)<=122:print(ch,"is small letter")
elif 48<=ord(ch)<=57:print(ch,"is digit")
else :print(ch,"is a symbol")
