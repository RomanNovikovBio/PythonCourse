import math
def rectangle(f,a,b,N):
    h = float((b - a)/N)
    result = f(a + 0.5*h)
    for i in range(1,N):
        result += f(a + 0.5*h + i*h)
    result *= h
    return result
