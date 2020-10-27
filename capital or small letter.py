#. wap to input a character and print whether it is capital or small letter
#. assume only alphabet is entered
ch=input("enter an alphabet\t:")
if ch>="A" and ch<="Z":print("{0} is capital letter".format(ch))
else:print("{0} is small letter".format(ch))

print()
if 65<=ord(ch)<=90:print("{0} is capital letter".format(ch))
else:print("{0} is small letter".format(ch))
