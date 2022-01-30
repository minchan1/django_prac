
# count = 0
# n = int(input())
# if (n-1)%
# if n%3==0:
#     n = n/3
#     count += 1
# if n%2==0:

# print(count)

# fibo = [0,1]
# n=int(input())
# for i in range(n):
#         fibo.append(fibo[i] + fibo[i+1])
# print(fibo[n])

# import re
# a = re.split('[-|+|*]', input())
# loc = []
# result=''
# temp = ''.join(i for i in a)
# for i in temp:

import re
temp = input()
buho = [i for i in temp if i=='-' or i=='+']
nums = re.split('[-|+|*]',temp)
for i in range(len(nums)):
    nums[i] = nums[i].lstrip('0')
for i in range(len(buho)):
    nums.insert(2*i+1,buho[i])
# print(nums)
data=''.join(nums)
# print(data)
# data = input()
result = 10**13
for i in range(len(data)):
    for j in range(i,len(data)+1):
        try:
            results = eval(data[:i] + '(' + data[i:j] + ')' + data[j:])
            result = min(result,results)
        except Exception as ex:
            continue
print(result)

