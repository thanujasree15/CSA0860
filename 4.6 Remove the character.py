def delchar(a,b):
    if len(b)!=1:
        return a
    else:
        return a.replace(b,"")
a=input("enter the word:")
b=input("enter the character to be removed:")
print(a)
print(delchar(a,b))
