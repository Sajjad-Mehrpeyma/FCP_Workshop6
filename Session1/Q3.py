import math
num=int(input())
first_digit=num%10
digits_num=int(math.log10(num))
last_digit=num//(10**digits_num)
mid=num - first_digit - (last_digit*(10**digits_num))
print(mid+(first_digit*(10**digits_num))+last_digit)
