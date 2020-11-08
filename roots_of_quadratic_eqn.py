#Program to find the roots of a quadratic equation
from math import *
a,b,c=[int(x) for x in input("enter a,b,c for ax2+bx+c=0\t:").split()]
det=b**2-4*a*c
print("determinant =",det)
if(det==0):
    x1=-b/(2*a)
    x2=-b/(2*a)
elif(det>0):
    x1=(-b+sqrt(det))/(2*a)
    x2=(-b-sqrt(det))/(2*a)
else:
    x1=complex(-b/(2*a),sqrt(-det)/(2*a))
    x2=complex(-b/(2*a),-sqrt(-det)/(2*a))
print(f"roots of {a}x2+{b}x+{c}=0 are {x1} and {x2}")
