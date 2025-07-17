#efficient for
arr=[4,-2,2,8,3,-3,1]

def summa(arr):
    if len(arr) <= 1:
        return arr      #return if 0 or 1 elemnt

    min_arr=min(arr)
    max_arr=max(arr)
    k=max_arr-min_arr+1

    #count list
    count=[0]*k

    for num in arr:
        count[num-max_arr]+=1

    sorted_arr=[]

    for i in range(k):
        sorted_arr.extend([i+min_arr]*count[i])
    return sorted_arr

print(summa(arr))