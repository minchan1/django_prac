# https://www.acmicpc.net/problem/2847

import sys

n = int(sys.stdin.readline())
nums = []
for _ in range(n):
    nums.append(int(sys.stdin.readline()))
nums.reverse()

ans = 0
for i in range(n-1):
    # 다음원소가 이전원소보다 크면,
    # 다음원소를 '이전원소의 값-1' 로 만들고
    # 차 만큼 ans에 합산
    if nums[i+1] >= nums[i]:
        ans += nums[i+1] - (nums[i]-1)
        nums[i+1] = nums[i]-1
print(ans)
