# https://www.acmicpc.net/problem/9012


def func(item):
    if item.count('(') != item.count(')'):
        print('NO')
        return
    if item[0] == ')' or item[-1] == '(':
        print('NO')
        return
    tmp = list(item)
    while tmp[0] == '(':
        tmp.remove('(')
        tmp.remove(')')
        if not tmp:
            break
        if tmp[0] == ')':
            print('NO')
            return
    print('YES')


n = int(input())
for _ in range(n):
    item = str(input())
    func(item)
