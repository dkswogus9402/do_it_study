def BFS(i, j):
    queue = [[i,j]]
    visited[i][j] = 1

    while queue:
        y, x = queue.pop(0)

        for dy, dx in ((0,1),(0,-1),(1,0),(-1,0)):
            ny = dy + y
            nx = dx + x
            if 0 <= ny<N and 0<=nx < N and visited[ny][nx] == 0 and A[ny][nx] == 1:
                queue.append([ny, nx])
                visited[ny][nx] = visited[y][x] + 1



A = [[0, 1, 1, 1, 0],
     [0, 1, 0, 0, 1],
     [0, 1, 1 ,1, 0],
     [1, 0, 1, 1, 0],
     [1, 0, 1, 1, 0]]
N = 5
visited = [[0] * N for _ in range(N)]
cnt = 0

for i in range(N):
    for j in range(N):
        if A[i][j] == 1 and visited[i][j] == 0:
            cnt += 1
            BFS(i,j)
print(cnt)