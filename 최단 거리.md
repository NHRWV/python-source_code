## 다익스트라 알고리즘

```python
import heapq
import sys


n, m = map(int, input().split())

start = int(input())

# 시작 지점, 도착 지점, 비용(가중치) 입력
info = [[] * (n+1) for _ in range(n+1)]
for i in range(m):
    a, b, t = map(int, input().split())
    info[a].append((b, t))
    
    
inf = int(1e9)
def dijk(start):
    distance = [inf] * (n+1)
    queue = []
    
    heapq.heappush(queue, (0, start)) # 우선순위 큐
    distance[start] = 0
    
    while queue:
        dist, node = heapq.heappop(queue)
        
        if distance[node] < dist: # 이미 처리된 노드라면 건너뛰기.
            continue
            
        for nxt, w in info[node]:
            cost = dist + w
            
            if cost < distance[nxt]: # 현재 노드를 거쳐서 다른 노드로 이동하는 거리가 더 짧은 경우.
                distance[nxt] = cost
                heapq.heappush(queue, (cost, nxt))
                
    return distance


dijk(start) # 함수 실행 후, distance 리스트의 값이 각각 노드까지의 최단 거리.

```




## 플로이드 와샬
