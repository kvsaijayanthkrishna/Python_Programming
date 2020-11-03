#lec-21/slide-19
#Write a function called cal_area() using default argument concept
#which accepts radius and pi as arguments and calculates and displays
#area of the Circle. The value of pi should be used as default argument
#and value of radius should be accepted from the user
import math
def cal_area(r,pi=math.pi):return pi*(r**2)
radius=int(input("enter radius of a circle\t:"))
print("area of a circle = {}".format(cal_area(radius)))
