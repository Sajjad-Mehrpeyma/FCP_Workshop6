d1, d2, d3 = input().split()
d1, d2, d3 = float(d1), float(d2), float(d3)

if d1 + d2 + d3 != 180 or d1 == 0 or d2 == 0 or d3 == 0:
    print('No')
else:
    print('Yes')
