t = int(input())

for _ in range(t):
    s = input()

    res = []

    for i in s:
        if i == "p":
            res.append('q')
        elif i == 'q':
            res.append('p')
        else:
            res.append('w')

    print("".join(res[::-1]))
        
