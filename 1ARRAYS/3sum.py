#define function------------
def thrsum(arr,target):
    map={}
    for i,num in enumerate(arr):
        map[num]=i
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            val=target-arr[i]-arr[j]
            if val in map and map[val]!=any([i,j]):
                return sorted([map[val],i,j])
    return()
#main fcn-----------------------------------------------
import time as t
t1=t.time()

param=[1,2,3,4,5,5,4,3,2,1]
print( thrsum(param,target=6) )

t2=t.time()
print(f"{1000*(t2-t1)}ms")#execution time in ms----------