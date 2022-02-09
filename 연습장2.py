
import math
n = int(input())
for _ in range(n):
    a,b = map(int,input().split())
    k = math.lcm(a,b)
    print(k)