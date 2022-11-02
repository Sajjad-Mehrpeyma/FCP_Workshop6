import math
def func(n):
    if n%2==0:
        return ((int(n/2)+1))**2
    else:
        return (int((((n-1)/2)+1)*(((n+1)/2)+1)))
func(3)
