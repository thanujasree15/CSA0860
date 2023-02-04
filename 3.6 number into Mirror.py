def reverse(s):
    str=""
    for i in s:
        str=i+str
    return str
s="sell123"
print("the original string is :",end="")
print(s)

print("the rversed string(with loops) is :",end="")
print(reverse(s))
