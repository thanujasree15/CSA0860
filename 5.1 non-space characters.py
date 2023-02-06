def length(str):
    lis=list(str.split(" "))
    return len(lis[-1])
str=input("enter the string to find the last word count: ")
print("the length of the last word is",length(str))

