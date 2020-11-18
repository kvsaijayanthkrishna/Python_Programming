
string=input("type a string\t:-")
dict1={}
for ch in string:
    count=string.count(ch)
    dict2={ch:count}
    dict1.update(dict2)
del dict2
for k,v in dict1.items():print(f"{k}:{v}")
print()
#with dictionary comprehension
mydict={ch:string.count(ch) for ch in string}
for k,v in mydict.items():print(f"{k}:{v}")
