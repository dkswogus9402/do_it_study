from collections import deque

N, M = map(int, input().split())
A = [list(map(int, input())) for _ in range(N)]

# 시작위치  = 0,0

s_y, s_x = 0, 0
e_y, e_x = N-1, M-1


visited = [[0] * (M) for _ in range(N)]

def bfs(s_y, s_x):
    queue = deque()
    queue.append([s_y, s_x])
    visited[s_y][s_x] = 1


    while queue:
       y,x =  queue.popleft()

       if y == e_y and x == e_x:
           return visited[y][x]


       for dy, dx in ((0,1), (0,-1), (1,0), (-1,0)):
           ny = dy + y
           nx = dx + x
           if 0 <= ny < N and 0 <= nx < M and visited[ny][nx] == 0 and A[ny][nx] != 0:
               queue.append([ny,nx])
               visited[ny][nx] = visited[y][x] + 1
    return -1

result = bfs(s_y, s_x)
print(result)