n, m, k = map(int, input().split(" "))

blocks = {}
for n in range(1, n+1):
    for m in range(1, m+1):
        name = str(n) + "A" + str(m)
        blocks[name] = []

for color in range(1, k+1):
    satr, sotoon, zel = map(int, input().split(" "))
    for a in range(satr, satr+zel):
        for b in range(sotoon, sotoon+zel):
            block = str(a) + "A" + str(b)
            blocks[block].append(color)

value_list = []
for value in blocks.values():
    if value != []:
        if value_list.count(value) == 0:
            value_list.append(value)

print(len(value_list))