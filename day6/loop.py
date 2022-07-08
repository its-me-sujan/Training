""" sum = 0
for i in range(1,16):
    sum+=i
print("{1} sujan befroe {0}".format(i,sum))
print(f"{i} {sum}")
print(sum)
"""
#print(sum(range(1,16)))
""" e_l= []
for i in range(1,51):
    if i%3 == 0:
        e_l.append(i)
print(f"the multiple of 3 are {e_l}")
"""
""" list = [i for i in range(3,51,3)]
print(list) """

""" list = [i for i in range(1,51) if i%3 == 0]
print(list) """

""" main = []
even = []
odd = []
duplicate = []
for i in range(15):
    num = int(input("Enter the nubmber "))
    if num not in main:
        if num%2 == 0:
            even.append(num)
        else:
            odd.append(num)
    else:
        duplicate.append(num)
    main.append(num)
print(main)
print(even)
print(odd)
print(duplicate) """

""" sum = 0
n = "12d567d895d56"
num = n.split("d")
print(num)
for i in num:
    sum += int(i)
print(sum)
"""
""" total = sum([int(i) for i in n.split("d")])
print(total) """


""" total = sum([i for i in range(1,51) if i% 4 == 0])
total = sum(range(4,51,4))
print(total) """