def profile(name,contact,address):
    print(f"Name    : {name}")
    print(f"Contact : {contact}")
    print(f"Address : {address}")

profile("Ram","98123","Ktm")#positional argument
print("******************")
profile(name="Ram",contact="98123",address="Ktm")