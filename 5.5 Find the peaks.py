def findpeakutil(arr,low,high,n):
  mid=low+(high-low)/2
  mid=int(mid)
  if((mid==0 or arr[mid-1]<=arr[mid])and(mid==n-1 or arr[mid+1]<=arr[mid])):
      return mid
  elif(mid>0 and arr[mid-1]>arr[mid]):
      return findpeakutil(arr,low,(mid-1),n)
  else:
      return findpeakutil(arr,(mid+1),high,n)
def findpeak(arr,n):
    return findpeakutil(arr,0,n-1,n)
arr=[1,2,3,1]
n=len(arr)
print("index of a peak point is",findpeak(arr,n))
