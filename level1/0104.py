# https://programmers.co.kr/learn/courses/30/lessons/12977
# 주어진 숫자 중 3개의 수를 더했을 때 소수가 되는 경우의 개수를 구하려고 합니다. 
# 숫자들이 들어있는 배열 nums가 매개변수로 주어질 때, nums에 있는 숫자들 중 서로 다른 3개를 골라 더했을 때 
# 소수가 되는 경우의 개수를 return 하도록 solution 함수를 완성해주세요.

import itertools

def solution(nums):
    nums_ = list(itertools.combinations(nums,3))
    for i in range(len(nums_)):
        nums_[i] = nums_[i][0] + nums_[i][1] + nums_[i][2]
    #nums_ = list(set(nums_))  # 중복 제거하면 안됨!! 다른 조합이면 다른 케이스로 봐야함
    answer = 0
    for n in nums_:
        for i in range(2,n):
            if n%i == 0:
                break
            else :
                if i == n-1:
                    answer += 1
                else :
                    continue    
    return answer