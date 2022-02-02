
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


from collections import deque
answer = 0
people=[70, 50, 80, 50]
limit=100
deq = deque(sorted(people))
# while deq:
#     if len(deq) == 1:
#         answer += 1
#         break
#     if deq[0] + deq[-1] <= limit:
#         deq.pop()
#         deq.popleft()
#     else:
#         deq.pop()
#     answer += 1
print(deque)

from collections import deque
def solution(people, limit):
    answer = 0
    deq = deque(sorted(people))
    while deq:
        if len(deq) == 1:
            answer += 1
            break
        if deq[0] + deq[-1] <= limit:
            deq.pop()
            deq.popleft()
        else:
            deq.pop()
        answer += 1
    return answer
