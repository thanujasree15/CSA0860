def romantoint(s):
    romandict={
        'I':1,
        'V':5,
        'X':10,
        'L':50,
        'C':100,
        'D':500,
        'M':1000
        }
    total=0
    i=0
    while i<len(s):
        if i+1<len(s) and romandict[s[i]]<romandict[s[i+1]]:
            total+=romandict[s[i+1]]-romandict[s[i]]
            i+=2
        else:
            total+=romandict[s[i]]
            i+=1
    return total
print(romantoint("III"))
print(romantoint("LVIII"))
print(romantoint("MCMXCIV"))
print(romantoint("LV"))

