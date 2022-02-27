# https://www.acmicpc.net/problem/5555

word = str(input())
k = len(word)
n = int(input())
ans = 0
for _ in range(n):
    tmp = str(input())
    tmp = tmp + tmp[:k-1]
    for i in range(len(tmp)-k+1):
        if tmp[i:i+k] == word:
            ans += 1
            break
print(ans)