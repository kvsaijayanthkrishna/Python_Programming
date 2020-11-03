#lec-21/slide-26
#Write a function called find_largest() which accepts multiple strings as argument
#and returns the length of the largest string
def find_largest(*string):
    largest_length=0
    for x in string:
        if(len(x)>largest_length):
            largest_length=len(x)
    return largest_length
print("largest_length=",find_largest("january","march","may","september"))
