def sumsquare(l):
    os=0
    es=0
    a=[]
    for i in l:
        if i%2==0:
            es+=i**2
        else:
            os+=i**2
    a.append(os)
    a.append(es)
    return a
n=int(input("enter the number of integers:"))
a=[]
for i in range(n):
    a.append(int(input("enter a integer:")))
print(a," is the original list")
s=sumsquare(a)
print(s)
