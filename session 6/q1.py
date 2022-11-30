def is_odd(n):
    return n % 2 == 1

def is_prime(n):
    if n == 2:
        return True
    
    for i in range(2, n//2):
        if n % i == 0:
            return False

    return True

def prime_divisors_number(n):
    prime_divisors_count = 0

    for i in range(2, n//2):
        if n % i == 0 and is_prime(i):
            prime_divisors_count += 1

    return prime_divisors_count

def is_khoshgel(n):
    prime_divisors = []
    
    if is_odd(n):
        for i in range(2, n//2):
            if n % i == 0 and is_prime(i):
                prime_divisors.append(i)

    prime_divisors_count = prime_divisors_number(n)
    
    if prime_divisors_count in prime_divisors:
        return True


    return False

n = int(input())
result = 0

for i in range(1, n+1):
    if is_khoshgel(i):
        result += i

if result != 0:
    print(str(result)[::-1])

else:
    print("NOT FOUND!")