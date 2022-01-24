import itertools
n,m = input().split()
cards = list(input().split())
for i in range(len(cards)):
    cards[i] = int(cards[i])
print(list(itertools.combinations(cards,3)))