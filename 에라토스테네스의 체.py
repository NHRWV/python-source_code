# n값이 소수인지 확인하는 함수.

import math

def is_prime_num(n):
    if n == 1:
        return 0
    
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return 0
    return 1
