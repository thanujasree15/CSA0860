string = "I am a python programmer "
words = string.split()
list1=list(words)
list2=[]
for i in list1[: : -1]:
    list2.append(i)
print(list2)
strconv=""
for x in list2:
    strconv+=' ' +x
print(strconv)
