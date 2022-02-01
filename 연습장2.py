
# import heapq
# def solution(scoville, K):
#     answer = 0
#     scoville.sort()
#     while scoville[0] < K:
#         if len(scoville) <= 1:
#             return -1
#         else:
#             small = heapq.heappop(scoville)
#             small2 = heapq.heappop(scoville)
#             heapq.heappush(scoville, (small + (small2 * 2)))
#             answer += 1
#     return answer



# numbers = [3, 30, 34, 5, 9]
# for i in range(len(numbers)):
#     numbers[i] = str(numbers[i])
# numbers.sort()
# loc = []
# for i in range(len(numbers)-1):
#     if numbers[i][0] != numbers[i+1][0]:
#         loc.append(i+1)

# print(loc)


n = list(input())
sum_ = 0
for i in n:
    sum_ += int(i)
if sum_%3==0 and '0' in n:
    n = sorted(n)
    # n.reverse()
    ans = ''
    for i in range(len(n)):
        ans=ans+n.pop()
    print(ans)
else:
    print(-1)
