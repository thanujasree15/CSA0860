s=input("enter the string 1: ")
t=input("enter the string 2: ")
if len(s)!=len(t):
    print("false")
else:
    a,b={},{}
    for i in range(len(s)):
        ch1,ch2=s[i],t[i]
        if ch1 not in a:
            a[ch1]=ch2
        if ch2 not in b:
            b[ch2]=ch1
        if a[ch1]!=ch2 or b[ch2]!=ch1:
            print("false")
            break
        else:
            print("true")
