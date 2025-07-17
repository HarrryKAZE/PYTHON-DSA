import datetime
now=datetime.now()
arr=[4,-2,2,8,3,-3,1]
max_val=max(arr)   # 8
min_val=min(arr)   # -3
k=abs(min_val)
count=[0]*(max_val+abs(min_val)+1)
for num in arr:
    count[k+num]+=1
print(arr)
ans=[]
for i,num in enumerate(count) :
    while num:
        ans.append(i-k)
        num-=1
print(ans)
then=datetime.now()
print(then-now)