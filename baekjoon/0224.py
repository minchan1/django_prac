# https://www.acmicpc.net/problem/9237

n = int(input())
tmp = list(map(int,input().split()))
tmp.sort(reverse=True)
ans = []
for i in range(len(tmp)):
    ans.append((i+2)+tmp[i])
print(max(ans))