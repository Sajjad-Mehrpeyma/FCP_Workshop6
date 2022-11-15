
age = int(input())

weight = int(input())

height = int(input())

skin_color = input()

hair_color = input()

glasses = False if input() == "Nadare" else True

mask = False if input() == "Nadare" else True

if not mask:
    print("Qaribas")
elif 15 <= age <= 45 and 60 <= weight <= 120 and ( 150 <= height <= 160 or 180 <= height <= 200) and (skin_color == "Sand" or skin_color == "Bronze") and (hair_color == "Black" or hair_color == "Brown") and not glasses:
    print("Ashnas")
elif 15 <= age <= 45 or 60 <= weight <= 120 or 150 <= height <= 160 or 180 <= height <= 200 or skin_color == "Sand" or skin_color == "Bronze" or hair_color == "Black" or hair_color == "Brown" or not glasses:
    print("Shayad")
else:
    print("Qaribas")