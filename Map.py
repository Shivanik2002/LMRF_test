def square(x):

    return x**2

a = map(square,[2,3,4,5])
print(list(a)) 

print("**************************")


def UpperCase(n):

    return n.upper()

Name = ("shivani","antim")
updated_tuple = map(UpperCase,Name)  
print(list(updated_tuple))

