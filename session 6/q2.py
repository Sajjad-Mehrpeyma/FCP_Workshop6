nummax = int(input())
n = 3
pi = 4
for i in range(nummax):
    if (i % 2 == 0):
        pi = pi - (4 / n)
        n = n+2

    else:
        pi = pi + (4 / n)
        n = n+2

print(pi)