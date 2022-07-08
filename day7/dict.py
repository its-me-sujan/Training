a = {"name":"dewansh","age":"12","faculty":"BCT"}
"""#accessing the value in dictionary
#using get
print(a.get("name"))
print(a)
print(a.get("name","sujan"))
print(a)
print(a.get("sex"))
print(a)
print(a.get("sex","M"))
print(a)

#setdefault
print(a.setdefault("name"))
print(a)
print(a.setdefault("name","sujan"))
print(a)
print(a.setdefault("sex"))
print(a)
print(a.setdefault("sex","M"))
print(a)"""

""" #loop in dict
for key in a.keys():
    print(key)
for value in a.keys():
    print(key)
for key,value in a.items():
    print(key,value)
"""