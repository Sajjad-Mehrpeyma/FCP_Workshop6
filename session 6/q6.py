def calculate_distance (place1, place2):
    # place1 ==> [3, 4, 2]
    # place2 ==> [3, -2, 0]

    result = (place1[0] - place2[0]) ** 2 + (place1[1] - place2[1]) ** 2 + (place1[2] - place2[2]) ** 2
    return result



x, y, z  = map(int, input().split())  # keikhosro

n = int(input())
p, k, z = map(int, input().split())


for i in range(n - 1):
    
    final_result = [p, k, z]
    
    p, k, z = map(int, input().split())
    distance = calculate_distance([x, y, z], final_result)

    if calculate_distance([x, y, z], [p, k, z]) < distance:
        final_result = [p, k, z]

print(final_result)

