def welcome():
    print("Mhrz loves iar,akahk!!")

#welcome -> call by reference
#welcome()

def add(x,y):
    print(x+y)
def sub(x,y):
    if x>y:
        print(x-y)
    else:
        print(y-x)
#x=int(input("Enter first numbers: "))
#y=int(input("Enter second number: "))
x,y = int(input("Enter two numbers")).split()
add(x,y)
sub(x,y)