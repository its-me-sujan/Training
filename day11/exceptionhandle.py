try:
    pass
except Exception:
    pass
else:
    pass

try:
    n1 = int(input("Enter number: "))
    n2 = int(input("Enter number: "))
except ValueError:
    print("cannot convert to integer")
except NameError:
    print("Variabel not defined")
else:
    print(n1+n2)