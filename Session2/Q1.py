#adad_pythagoras

a = int(input())
b = int(input())
c = int(input())

sides = []
sides.append(a)
sides.append(b)
sides.append(c)

sides.sort()

if sides[0]**2 + sides[1]**2 == sides[2]**2:
    print("YES")

else:
    print("NO")
