# print("It's a whole new world")
num1 = int(input("Enter an integer: "))
if num1%3 == 0:
    print("{} is divisible by 3!".format(num1))
elif num1%5 == 0:
    print("{} is divisible by 5!".format(num1))
elif num1%7==0:
    print("{} is divisible by 7!".format(num1))
else:
    None
