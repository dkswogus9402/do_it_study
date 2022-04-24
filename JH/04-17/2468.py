from collections import deque

def BFS(i, j, height):
    queue = deque()
    queue.append([i, j])
    visited[i][j] = 1

    while queue:
        y, x = queue.popleft()

        for dy, dx in ((0,1),(0,-1),(1,0),(-1,0)):
            ny, nx = dy + y, dx + x
            if 0 <= ny < N and 0 <= nx < N and visited[ny][nx] == 0:
                if A[ny][nx] >= height:
                    queue.append([ny,nx])
                    visited[ny][nx] = 1

N = int(input())

A = [list(map(int, input().split())) for _ in range(N)]
a = set()
for i in range(N):
    for j in range(N):
        a.add(A[i][j])
max_cnt = 0
height = [1] + list(a)

for h in height:
    visited = [[0] * N for _ in range(N)]
    cnt = 0
    for i in range(N):
        for j in range(N):
            if A[i][j] >= h and visited[i][j] == 0:
                cnt += 1
                BFS(i, j, h)
    if max_cnt < cnt:
        max_cnt = cnt

print(max_cnt)