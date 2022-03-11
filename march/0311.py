# https://www.acmicpc.net/problem/2331

a,p = map(int,input().split())
nums = [a]

# 주어진 수열의 다음 원소를 구하는 함수
# a의 각 자리의 숫자를 p제곱하여 더함
def func(x):
    tmp = list(str(x))
    k = 0
    for i in tmp:
        k += int(i)**p
    return k

# 중복인 숫자가 나올때 까지 수열 진행  
while True:
    n = func(a)
    if n not in nums:
        nums.append(n)
    else:
        index_to_del = nums.index(n)
        break
    a = n

# 중복된 숫자가 처음 시작된 부분부터 삭제
del nums[index_to_del:]
print(len(nums))