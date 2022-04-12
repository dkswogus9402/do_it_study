from collections import deque

def BFS(i, j):
    cnt_N = 1
    queue = deque()
    queue.append([i,j])
    visited[i][j] = 1
    value = A[i][j]

    while queue:
        y,x = queue.popleft()

        for dy, dx in ((0,1),(0,-1),(1,0),(-1,0)):
            ny = dy + y
            nx = dx + x
            if 0<=ny<N and 0<=nx<N and visited[ny][nx] == 0 and value == A[ny][nx]:
                visited[ny][nx] = 1
                queue.append([ny, nx])
                cnt_N += 1
    return cnt_N


N = int(input())
A = [list(map(int, input())) for _ in range(N)]

visited = [[0] * N for _ in range(N)]
cnt = 0
result = []
for i in range(N):
    for j in range(N):
        if A[i][j] != 0 and visited[i][j] == 0:
            cnt_N = BFS(i,j)
            result.append(cnt_N)
            cnt += 1

print(cnt)
result.sort()
for i in result:
    print(i)