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

# 오일러 피(파이) 함수 ϕ(n) 란 1과 n까지의 정수 중 n과 서로소인 개수를 뜻한다.
# 즉, 자신보다 작은 양수 중에서 자기 자신과의 최대 공약수가 1인 숫자가 몇 개인지 알아보는 것.
