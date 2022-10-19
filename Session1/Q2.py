import math
a,b,c,d,e=map(float,input().split())
avg=(a+b+c+d+e)/5
sigma=(math.pow((a-avg),2)+math.pow((b-avg),2)+math.pow((c-avg),2)+math.pow((d-avg),2)+math.pow((e-avg),2))/5
sdt=math.sqrt(sigma)
print(round(sdt,3))
