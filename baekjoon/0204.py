# https://www.acmicpc.net/problem/2941

word = input()
tmp = len(word)
cnt = 0
cro = ['c=','c-','dz=','d-','lj','nj','s=','z=']
for i in cro:
    if i in word and i != 'z=':
        cnt += word.count(i)
        tmp -= len(i)*word.count(i)
    elif i in word and i == 'z=':
        cnt += word.count(i) - word.count('dz=')
        tmp -= len(i)*word.count(i)
        tmp += word.count('dz=')*2
print(cnt+tmp)

# https://www.acmicpc.net/problem/2751

from sys import stdin
# 입력 여러개 받을때 시간단축
from collections import deque
# deque를 써서 시간단축
n = int(stdin.readline())
nums = []
for i in range(n):
    nums.append(int(stdin.readline()))
nums = deque(sorted(nums))
for i in range(n):
    print(nums.popleft())