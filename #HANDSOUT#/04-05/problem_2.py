N = 4
pos = [[1,0], [-1,0], [0, 1], [0, -1]]

A = [[0, 0, 0, 1],
     [0, 1, 0, 0],
     [0, 0, 0 ,0],
     [0, 0, 0, 1]]


visited = [[0] * N for _ in range(N)]
queue = []
for i in range(N):
    for j in range(N):
        if A[i][j] == 1:
            queue.append([i, j])
            visited[i][j] = 1

while queue:
    y, x = queue.pop(0)

    for dy, dx in pos:
        ny = dy + y
        nx = dx + x
        if 0 <= ny < N and 0 <= nx < N and visited[ny][nx] == 0:
            queue.append([ny, nx])
            visited[ny][nx] = visited[y][x] + 1

for a in visited:
    print(a)