# 기본적인 이분 매칭을 위한 코드는 다음과 같다.
# 가장 대표적인 축사 배정 코드.

n, m = map(int, input().split())
lst = [[]]
for i in range(n):
    lst.append(list(map(int, input().split()))[1:])
    
barn = [0] * (m+1)

def sol(x):
    if visited[x]:
        return False
    
    visited[x] = 1
    for i in lst[x]:
        if not barn[i] or sol(barn[i]): # 배정하고자 하는 축사가 비어 있거나,  
            barn[i] = x                  # 기존에 배정된 소가 갈 수 있는 다른 칸이 남아있는 경우
            return True

    return False


count = 0
for i in range(1, n+1):
    visited = [0] * (n+1)
    if sol(i):
      count += 1
      
print(count)



#그런데 때로는 이분 매칭하는 그룹의 정점을 직접 만들어야 할 때가 있다. 
# 가장 대표적인 게 룩 시리즈다. 
# 다음은 N-Rook 문제의 코드다.

n, m = map(int, input().split())

board = []
for i in range(n):
    board.append(list(map(int, input().split())))
    

ref = [[0] * m for _ in range(n)] # 행 기준으로 번호를 부여할 행렬
ref2 = [[0] * m for _ in range(n)] # 열 기준으로 번호를 부여할 행렬


num = 1    
for i in range(n):
    check = False
    for j in range(m):
        if board[i][j] == 0 or board[i][j] == 1:
            ref[i][j] = num
            check = True
        
        else:
            if check:
                num += 1
                check = False
    
    if check:
        num += 1    
        
        

edge = [[] for _ in range(num)]   # 행에서 열로 이분 매칭할 것임으로 반드시 지금 num 수로 인접 리스트를 만들어 준다.

# 이제 열을 기준으로 번호를 부여한다.
num = 1    
for j in range(m):
    check = False
    for i in range(n):
        if board[i][j] == 0 or board[i][j] == 1:
            ref2[i][j] = num
            check = True
        
        else:
            if check:
                num += 1
                check = False
                
    if check:
        num += 1
    

    
for i in range(n):
    for j in range(m):
        if board[i][j] == 0:
            edge[ref[i][j]].append(ref2[i][j]) # 인접 리스트 만들기. 이걸 바탕으로 이분 매칭을 할 것이다.
            
            
target = [0] * num  # 열 기준으로 번호를 부여했을 때의 num 값으로 배열 생성.

def sol(x):
    if visited[x]:
        return False
    
    visited[x] = 1
    for i in edge[x]:
        if target[i] == 0 or sol(target[i]):
            target[i] = x
            return True
        
    return False


count = 0
for i in range(1, len(edge)):
    visited = [0] * len(edge)
    if sol(i):
        count += 1
        
print(count)
