#taghvim shamsi

year, month, day = map(int, input().split("/"))
is_leap_year = False

remainder = year % 33
allow_year_remainders = [1, 5, 9, 13, 17, 22, 26, 30]
if remainder in allow_year_remainders:
    is_leap_year = True


if not 1 <= month <=12:
    print("month number is not valid!")

elif 1 <= month <= 6 and not 0 < day < 32:
    print("day number is not valid!")

elif 6 <= month <12 and not 0 < day < 31:
    print("day number is not valid!")

elif is_leap_year and not 0 < day < 31:
    print("day number is not valid!")

elif not is_leap_year and not 0 < day < 30:
    print("day number is not valid!")

else:
    month_names = ["farvardin", "ordibehesht", "khordad", "tir", "mordad", "shahrivar", "mehr", "aban", "azar", "dey", "bahman", "esfand"]
    month_name = month_names[month-1]
    if 0 < month < 7:
        num_days = 31
    elif 6 < month < 12:
        num_days = 30
    elif (is_leap_year):
        num_days = 30
    else:
        num_days = 29
    num_week = day // 7 + 1
    
    if day % 7 == 0:
        num_week -= 1
    
    if (is_leap_year):
        print("leap year")
    else:
        print("not leap year")
    print(month_name)
    print(num_days)
    print(num_week)
        
    
