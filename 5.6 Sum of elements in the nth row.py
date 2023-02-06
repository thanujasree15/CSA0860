from math import factorial
n = int(input("Enter no.of rows:"))
n2=int(input("Enter the row number:"))
s=0
for i in range(n):
    for j in range(n-i+1):

        print(end=" ")

    for j in range(i+1):
            a=(factorial(i)//(factorial(j)*factorial(i-j)))
            if n2==i+1:
                s=s+a
               
            print(a,end=" ")
    print()
print()
print("The sum of the given row is ",s)
