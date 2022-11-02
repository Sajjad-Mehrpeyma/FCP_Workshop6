h,f,d=map(int,input().split())
discount=int(input())
total=h*5+f*3+d
print(f'hamburger: {h} -> {h*5}$')
print(f'french fries: {f} -> {f*3}$')
print(f'drink: {d} -> {d}$')
print(f'total: {total}$')
print(f'discount: {total*discount/100}')
print(f'pay: {total - total*discount/100}$')
