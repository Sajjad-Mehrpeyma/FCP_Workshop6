x1,y1,x2,y2 = map(float,input().split())
print("%.5f"%((x2-x1)**2+(y2-y1)**2)**0.5)
print("%.5f %.5f"%((x1+x2)/2,(y1+y2)/2))
