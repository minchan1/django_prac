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