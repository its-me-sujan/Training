""" username = "r@gmail.com"
password = "123@abcd"
uname = input("Enter username: ")
pw = input("Enter password: ")
while uname!=username or pw!=password:
    uname = input("Enter username: ")
    pw = input("Enter password: ")
else:
    print("User Matched!!!")
"""
a = [(1,2,3),(5,6,7),(8,9,0)]
total = 0
for i in a:
    total+=int("".join([str(j) for j in i]))
print(total)