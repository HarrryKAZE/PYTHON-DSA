def noduplicaaates(nums):
    i,j=0,1
    while nums[i] and nums[j-1] and nums[j-1]!=nums[-1]:
        if nums[i]!=nums[j]:
            i+=1
            nums[i]=nums[j]
        else:j+=1
    return (nums[:i+1])

#main fcn
nums=[3,4,4,5,5,6,7,8]
import time as t
t1=t.time()

print(noduplicaaates(nums))

t2=t.time()
print(f"{1000*(t2-t1)}ms")#execution time in ms 0.4-0.9 ms