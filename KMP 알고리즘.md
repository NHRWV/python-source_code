문자열과 패턴(서브 문자열)이 있을 때 문자열 안에서 패턴이 존재하는지 알아내는 알고리즘.

시간 복잡도는 O(n)이다.

``` python
def get_pi(pattern):
    pi = [0] * len(pattern)
    idx = 0
    
    for i in range(1, len(pattern)):
        while idx > 0 and pattern[i] != pattern[idx]:
            idx = pi[idx - 1]
            
        if pattern[i] == pattern[idx]:
            idx += 1
            pi[i] = idx
            
    return pi

# get_pi 함수는 패턴의 길이만큼 접미사가 일치하는 최대 개수를 반환한다.
# 예를 들어, 패턴이 abacaba 라면 pi = [0, 0, 1, 0, 1, 2, 3]이 된다.
# 다시 말하자면 해당 인덱스의 글자까지 봤을 때, 앞과 뒤가 일치하는 길이를 의미한다.


# 0...a 앞의 숫자에 주목
# 0...ab
# 1...aba
# 0...abac
# 1...abaca
# 2...abacab
# 3...



def kmp(s, pattern):  # 패턴 파악. s는 문자열이다.
    n = len(s)
    m = len(pattern)
    
    pi = get_pi(pattern)
    idx = 0
    for i in range(n):
        while idx > 0 and s[i] != pattern[idx]:
            idx = pi[idx - 1]
            
        if s[i] == pattern[idx]:
            if idx == m - 1:
                return True
            else:
                idx += 1
                
    return False

```

