
price_buy = int(input())
price_current = int(input())
count = int(input())

if not ( 1000 <= price_buy <= 100000 and 1000 <= price_current <= 100000 and 50 <= count <= 5000 and price_buy % 10 == 0 and price_current % 10 == 0 and count % 10 == 0):
    print("Invalid Input")
else:
    if price_current >= price_buy:
        print("Profit")
    else:
        print("Loss")
    
    profit_rate = (price_current - price_buy) / price_buy * 100
    print(f"{profit_rate:+.2f}")
    if price_current * count > 5000000 and profit_rate > 20:
        print("Lucky")
    elif price_current * count <= 5000000 or 0 <= profit_rate <= 20:
        print("Normal")
    elif price_buy * count < 10000000 and 0 > profit_rate > -20:
        print("Chance")
    elif price_buy * count >= 10000000 and profit_rate <= -20:
        print("under the coverage")