
#     if len(deq) == 1:
#         answer += 1
#         break
#     if deq[0] + deq[-1] <= limit:
#         deq.pop()
#         deq.popleft()
#     else:
#         deq.pop()
#     answer += 1