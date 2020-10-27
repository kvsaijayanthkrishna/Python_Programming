#. WAP to check whether entered year is leap year or not
year=int(input("enter a year\t:"))
if not(year%100) and not(year%400):print(year,"is leap year")
elif not(year%4) and year%100:print(year,"is a leap year")
else:print(year,"is not a leap year")
