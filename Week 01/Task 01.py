a=input("enter the string:")
b=""
for i in a:
    i=i.lower()
    if i.isalpha():
        a=ord(i)-96
        b=b+str(a)+" "
print(b)
