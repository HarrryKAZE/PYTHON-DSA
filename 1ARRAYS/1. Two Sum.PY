def two_sum(nums,target):
    map={}
    ans=[]
    for i, num in enumerate(nums):
        map[num]=i                      #create hash map for o(1) lookup of unsorted array
    for i, num in enumerate(nums):
        val=target-num
        if val in map and map[val]!=i and [map[val],i] not in ans:#check the index and pair only 1 time
            ans.append([i,map[val]])
    return ans
arr=[1,2,3,4,5]
print(two_sum(arr,target=6))