# https://www.acmicpc.net/problem/1302

n = int(input())
books = {}
for _ in range(n):
    i = str(input())
    if i in books:
        books[i] += 1
    else:
        books[i] = 1
tmp = [k for k,v in books.items() if max(books.values()) == v]
tmp.sort()
print(tmp[0])