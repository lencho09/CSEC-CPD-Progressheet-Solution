from collections import Counter
n = int(input())
lst = []
for _ in range(n):
    s = input()
    lst.append(s)

count = Counter(lst)
large = 0 
res = None
for key, value in count.items():
    if value > large:
        large = value
        res = key
print(res)
