# https://www.acmicpc.net/problem/1094

stk = [64]
x = int(input())
while sum(stk)!=x:
    if sum(stk) > x:
        min_ = int(min(stk)/2)
        stk.remove(min(stk))
        stk.append(min_)
        if sum(stk) < x:
            stk.append(min_)
print(len(stk))
    