소스코드 예시
수정 예정

``` python
def KMP(P,T):
    ans=[]
    lt=len(T)
    lp=len(P)
    table=makeTable(P)
    i=0
    for j in range(lt):
        while i>0 and P[i]!=T[j]:
            i=table[i-1]
        if P[i]==T[j]:
            if i==lp-1:
                ans.append(j-lp+2)
                i=table[i]
            else:
                i+=1
    return ans
```

