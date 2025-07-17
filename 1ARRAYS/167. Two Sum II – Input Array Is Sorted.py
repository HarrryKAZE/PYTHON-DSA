#define function------------
def twosumsor(arr,target):
    seen={}
    for i,num in enumerate(arr):
        val=target-num
        if val in seen: return (seen[val],i)
        seen[num]=i



#main fcn-----------------------------------------------
import time as t
t1=t.time()

param=[1,2,3,4,5]
print( twosumsor(param,target=5) )

t2=t.time()
print(f"{1000*(t2-t1)}ms")#execution time in ms----------