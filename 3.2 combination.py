def comb(L):
    for i in range(3):
        for j in range(3):
            for k in range(3):
                if(i!=j and j!=k and k!=i):
                    print(L[i],L[j],L[k])
n=(input("enter the number: "))
if(n==n):
    comb(n)
                
            
