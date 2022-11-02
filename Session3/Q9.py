a,b=map(int,input().split())
oper=input()
c,d=map(int,input().split())

real_out=img_out=0
if oper=='+':
    real_out=a+c
    img_out=b+d
elif oper=='-':
    real_out=a-c
    img_out=b-d
elif oper=='*':
    real_out=a*c-b*d
    img_out=a*d+b*c
elif oper=='/':
    real_out=(a*c + b*d)/(c**2+d**2)
    img_out=(b*c-a*d)/(c**2+d**2)
print(f'({round(real_out,2)})+({round(img_out,2)})i')
