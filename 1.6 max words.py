a=input ("enter the sentences:")
m=input ("enter the sentences:")
r=input ("enter the sentences:")
i=input ("enter the sentences:")
b=a.split ()
c=len (b)
d=m.split ()
e=len (d)
f=r.split()
g=len (f)
h=i.split ()
j=len (h)
if c>e and c>g and c>j:
    print (a, "has", c, "and it is the maximum number of words")
if e>c and e>g and e>j:
    print (m, "has",e, "the maximum number of words")
if g>c and g>e and g>j:
    print (r, "has", g, "the maximum number of words")
else:
    print (i, "has", j, "the maximum number of words")
