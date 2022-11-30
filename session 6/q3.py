x = int(input())
list1 = list(map(int, input().split()))
list2 = list(map(int, input().split()))

list2.reverse()

result = 0

for index in range(1, len(list1)+1):
    number1 = list1[-index]
    number2 = list2[-index]

    digit = number1 + number2

    if digit > 9:
        result += (digit-10) * 10 ** (index-1)
        result += 10 ** index

    else:
        result += digit * 10 ** (index-1)

print(result)

