def FindPrimes(n):
    numbers = list(range(0, int(n+1)))
    
    max_element = numbers[n]
    mult_counter = 2
    for prime in numbers[2:]:
        if prime !=0:
            while mult_counter * prime <= max_element:

                numbers[mult_counter * prime] = 0
                mult_counter += 1

            mult_counter = 2
    
    result = []
    for number in numbers[2:]:
        if number != 0:
            result.append(number)

    return(result)

print(FindPrimes(100))