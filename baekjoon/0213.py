# https://www.acmicpc.net/problem/1292

nums = []
n=0
a,b=map(int,input().split())
while True:
    n+=1
    for _ in range(n):
        nums.append(n)
        if len(nums)==1000:
            break
    if len(nums)==1000:
        break
print(sum(nums[a-1:b]))