# https://www.acmicpc.net/problem/1259

while True:
    n = int(input())
    if n == 0:
        break
    tmp = str(n)
    new_num = int(tmp[-1:-(len(tmp)+1):-1])
    if new_num == n:
        print('yes')
    else:
        print('no')
