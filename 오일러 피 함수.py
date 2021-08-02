# 어렵다

def Euler(n):
    phi = n
    for i in range(2, int(n**(1/2) + 1)):
        if n % i == 0:
            phi -= phi // i
            while n % i == 0:
                n //= i
    
    if n > 1:
        phi -= phi // n
    return phi
