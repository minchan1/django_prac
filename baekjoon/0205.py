# https://www.acmicpc.net/problem/1427

n = list(input())
n.sort(reverse=True)
ans = ''
for i in n: ans = ans+i
print(ans)