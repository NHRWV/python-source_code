import sys
# input = lambda: sys.stdin.readline().rstrip()

inf = int(1e9)

class SegmentTree:
    def __init__(self, data, default=10**15, func=lambda a, b: max(a,b)):
        """initialize the segment tree with data"""
        self._default = default
        self._func = func
        self._len = len(data)
        self._size = _size = 1 << (self._len - 1).bit_length()
 
        self.data = [default] * (2 * _size)
        self.data[_size:_size + self._len] = data
        
        for i in reversed(range(_size)):
            self.data[i] = func(self.data[i + i], self.data[i + i + 1])
 
    def __delitem__(self, idx):
        self[idx] = self._default
 
    def __getitem__(self, idx):
        return self.data[idx + self._size]
 
    def __setitem__(self, idx, value):
        idx += self._size
        self.data[idx] = value
        idx >>= 1
        
        while idx:
            self.data[idx] = self._func(self.data[2 * idx], self.data[2 * idx + 1])
            idx >>= 1
 
    def __len__(self):
        return self._len
 
    def query(self, start, stop):
        if start == stop:
            return self.__getitem__(start)
        
        stop += 1
        start += self._size
        stop += self._size
 
        res = self._default
        while start < stop:
            if start & 1:
                res = self._func(res, self.data[start])
                start += 1
            if stop & 1:
                stop -= 1
                res = self._func(res, self.data[stop])
            start >>= 1
            stop >>= 1
        return res
 
    def __repr__(self):
        return "SegmentTree({0})".format(self.data)
    
    
    
n, m = map(int, input().split()) # n : 배열 길이, m : 쿼리 수 
lst = [int(input()) for _ in range(n)] # 배열 입력 받기.

func = lambda a, b: a + b # 최댓값 구하는 경우 max(a, b)
seg = SegmentTree(lst, 기본 값 (덧셈시 0, 최댓값시: -inf, 최솟값시: inf, func = func)

# seg.query(구간 시작, 구간 끝)
                  
# 사용 예시
# b번째 숫자를 c로 바꾸기 : seg[b] = c
# b부터 c까지의 연산 : seg.query(b, c)
