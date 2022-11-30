def factorial(n):
    if n == 0 or n ==1 :
        return 1
    
    if n == 2:
        return 2

    else:
        for i in range(2, n):
            n = n * i

    return n


def cos(x):
    result = 1
    for i in range(50):
        result += ((-1) ** (i+1)) * (x ** ((i + 1) * 2)) / factorial((i + 1) * 2)
    
    return result


f, d, theta = map(float, input().split())
theta = theta * 3.14 / 180
result = f * d * cos(theta)

print(f'{result:.2f}')