# https://www.acmicpc.net/problem/10162
# A 300 , B 60 ,  C 10

T = int(input())
count_A = 0
count_B = 0
count_C = 0
if T%10 != 0:
    print(-1)
else:
    while T!=0:
        if T >= 300:
            T -= 300
            count_A += 1
            continue
        elif T >= 60:   
            T -= 60 
            count_B += 1
            continue
        elif T >= 10:
            T -= 10
            count_C += 1 
    print('{0} {1} {2}'.format(count_A,count_B,count_C))

# https://www.acmicpc.net/problem/11399

n,Pi = input(),input()
n = int(n)
Pi = list(Pi.split())
for i in range(n):
    Pi[i] = int(Pi[i])
Pi_ = sorted(Pi)
time = 0
total = 0
for i in range(n):
    time = time + Pi_[i]
    total += time
print(total)