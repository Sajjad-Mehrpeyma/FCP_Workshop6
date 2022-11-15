n = int(input())

num = n // 4

if n % 4 == 0:
    print(f"{-num} {num}")
elif n % 4 == 2:
    print(f"{num + 1} {-num}")
elif n % 4 == 3:
    print(f"{num + 1} {num + 1}")
else:
    print(f"{-num} {-num}")

