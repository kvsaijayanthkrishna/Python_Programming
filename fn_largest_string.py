#lec-21/slide-28
#Write a function called find_largest() which accepts multiple strings as argument
#and returns the largest string
def find_largest(*string):
    largest_length=0
    largest=""
    for x in string:
        if(len(x)>largest_length):
            largest=x
    return largest
print("largest string=",find_largest("january","march","may","september"))
