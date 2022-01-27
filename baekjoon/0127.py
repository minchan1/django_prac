# 그리디
# 틀림 -> 확인필요
# https://www.acmicpc.net/problem/1541


import re
temp = input()
buho = [i for i in temp if i=='-' or i=='+']
nums = re.split('[-|+|*]',temp)
for i in range(len(nums)):
    nums[i] = nums[i].lstrip('0')
for i in range(len(buho)):
    nums.insert(2*i+1,buho[i])
# a = list(input())
a = nums
loc = []
result=''
for i in range(len(a)):
    if a[i]=='-':
        loc.append(i)
for i in range(len(loc)):
    if i%2==0:
        a.insert(loc[i]+1,'(')
    else:
        a.insert(loc[i]-1,')')
if a.count('(')%2!=0:
    a.append(')')
for i in a:
    result += i
for i in result:
    try: i = int(i)
    except: pass
print(eval(result))



