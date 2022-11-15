name, number = input().split()
number = float(number)
if name == 'apple':
    result = int(100*number)
elif name == 'banana':
    result = int(250*number)
elif name == 'peach':
    result = int(70*number)
elif name == 'lemon':
    result = int(45*number)
elif name == 'kiwi':
    result = int(85*number)

print(result)
if result < 100:
    print('less')
elif 100 <= result <= 200:
    print('ok')
else:
    print('more')