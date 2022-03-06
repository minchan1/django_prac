# https://www.acmicpc.net/problem/1764

n, m = map(int,input().split())
name1 = {input() for _ in range(n)}   
name2 = {input() for _ in range(m)}
ans = list(name1 & name2)
ans.sort()     
print(len(ans))
for name in ans:
    print(name)