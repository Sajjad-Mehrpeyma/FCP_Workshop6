x1,y1=map(float,input().split())
x2,y2=map(float,input().split())
d=((x1-x2)**2+(y1-y2)**2)**0.5
print(f'(X1,Y1) = ({x1},{y1})')
print(f'(X2,Y2) = ({x2},{y2})')
print(f'Diff = {round(d,2)}')
