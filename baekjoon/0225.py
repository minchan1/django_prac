# https://www.acmicpc.net/problem/11170

n = int(input())
for _ in range(n):
    nums = []
    tmp = ''
    a,b=map(int,input().split())
    for i in range(a,b+1):
        nums.append(i)
    for num in nums:
        tmp+= str(num)
    ans = list(tmp)
    print(ans.count('0'))
