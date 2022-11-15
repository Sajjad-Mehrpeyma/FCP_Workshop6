
score = int(input())


num_vacation = int(input())

if num_vacation == 0:
    score = 20

elif num_vacation == 7:
    pass

else:
    score -= num_vacation

if score < 0:
    score = 0

print(score)