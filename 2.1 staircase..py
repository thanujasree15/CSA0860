def fib(n,dp):
    if(n<=1):
        return 1
    if(dp[n]!=1):
        return dp[n]
    dp[n]=fib(n-1,dp)+fib(n-2,dp)
    return dp[n]
def countway(n):
    dp=[1 for i in range(n+1)]
    fib(n,dp)
    return dp[n]
n=int(input("enter a number"))
print("number of ways"+str(countway(n)))
