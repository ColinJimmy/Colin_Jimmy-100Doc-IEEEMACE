def square_sum():
    l=eval(input("enter the array:"))
    a=0
    for i in l:
        a+=int(i**2)
    return a
print(square_sum())
