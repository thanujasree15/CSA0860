s=input('enter a string:')
dc=0
ac=0
for i in s:
    if i.isalpha():
        ac+=1
    if i.isdigit():
        dc+=1
    print('no. of digits:',dc)
    print('no. of alphabets:',ac)
        
