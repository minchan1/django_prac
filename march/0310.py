# https://www.acmicpc.net/problem/11656

word = str(input())
tmp = []
n = 0
while n!=len(word):
    tmp.append(word[n:])
    n+=1
tmp.sort()
for i in tmp:
    print(i)