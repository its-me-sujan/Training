""" def my_fun(*args):
    for i in args:
        print(i)

my_fun(1,2,3) """

""" def fun(**kwargs):
    for key,value in kwargs.items():
        print(f"{key} : {value}")
fun(name="dewansh",roll="12",cont="98766")
"""
# def my_fun(*args,**kwargs):
#     print(args)
#     print(kwargs)
# my_fun(1,2,3,name="Ram",roll="43")

# def fun(name,roll,cont):
#     print(name)
#     print(roll)
#     print(cont)

# pro = {"name":"dewansh","roll":"12","cont":"9887"}
# fun(**pro)