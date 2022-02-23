# https://www.acmicpc.net/problem/14916

n = int(input())
def func(n):    
    ans = 0
    if n==1 or n==3:
        return -1
    if (n%5)%2==0:
        ans += n//5
        n = n%5
    else:
        ans += (n//5) -1
        n = (n%5) + 5
    ans += n//2
    return ans

print(func(n))