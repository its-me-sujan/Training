# def welcome(name):
#     print(f"Welcome {name}")
# def greet_ram(func):
#     func("ram")

# greet_ram(welcome)

#print(type(welcome))
# def add(a,b):
#     print(a+b)

# a = add
# a(10,12)

# def square_root_of_num(func,num1,num2):
#     return func(num1,num2)**0.5

# def add (num1, num2):
#     return num1+num2
# print(square_root_of_num(add,10,15))

# def cube_root_of_sum(func,num1,num2,num3):
#     return func(num1,num2,num3)**(1/3)

# def add (num1, num2, num3):
#     return num1+num2+num3
# print(cube_root_of_sum(add,10,15,2))

# def outer_func():
#     def first_child():
#         print("I am first child")
#     def second_child():
#         print("I am second child")
#     first_child()
#     second_child()

# outer_func()



# def calculator(operator):
#     def add(a,b):
#         return a+b
#     def product(a,b):
#         return a*b
#     if operator == "+":
#         return add
#     elif operator == "*":
#         return product
# totalsum = calculator("+")
# multiplication = calculator("*")
# print(totalsum(10,15))
# print(multiplication(10,15))

def calculator(operator,a,b):
    def add():
        return a+b
    def product():
        return a*b
    if operator == "+":
        return add
    elif operator == "*":
        return product
a = calculator("+",10,15)
b = calculator("*",10,15)

print(a())
print(b())