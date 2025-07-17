# 88. Merge Sorted Array 
#define function------------
def mergesorted(arr):
    i,j=0,0
    m=len(arr[0])
    n=len(arr[1])
    while i<m and j<n:
        if arr[0][i]<=arr[1][j]:
            i+=1
        else:
            arr[0][i]=arr[1][j]
            arr[1].sort()
    
    return (arr[0]+arr[1])

#main fcn-----------------------------------------------
import time as t
t1=t.time()

param=[[1,1,2,3,4,5,6],[1,4,6,7,7,7]]
print( mergesorted(param) )

t2=t.time()
print(f"{1000*(t2-t1)}ms")#execution time is 0.98 ms----------



#approach no2 
# 88. Merge Sorted Array 
#define function------------
def mergesorted(arr):
    i,j=0,0
    m=len(arr[0])
    n=len(arr[1])
    ans=[]
    while i<m and j<n:
        if arr[0][i]<=arr[1][j]:
            ans.append(arr[0][i])
            i+=1
        else:
            ans.append(arr[0][j])
            j+=1
    ans.extend(arr[0][i:])
    return ans.extend(arr[0][j:])

#main fcn-----------------------------------------------
import time as t
t1=t.time()

param=[[1,1,2,3,4,5,6],[1,4,6,7,7,7]]
print( mergesorted(param) )

t2=t.time()
print(f"{1000*(t2-t1)}ms")#execution time in  0.586ms---------