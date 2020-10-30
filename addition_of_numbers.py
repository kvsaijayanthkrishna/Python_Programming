#lec-18/slide-20 Write a program to continuously accept integers from the user until
#the user types 0 and as soon as 0 is entered display sum of all the nos entered before 0
n=int(input("enter a number(press 0 to stop)\t:"))
sum=0
while n!=0:
    sum+=n
    n=int(input("enter a number(press 0 to stop)\t:"))
print("Sum is",sum)
