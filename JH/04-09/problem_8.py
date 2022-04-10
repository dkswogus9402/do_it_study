def BFS():
    while queue:
        y, x = queue.pop(0)

        if A[y][x] == 2:
            return visited[y][x]

        for dy, dx in ((0,1), (0,-1), (1,0), (-1,0)):
            ny = dy + y
            nx = dx + x
            if 0 <= ny < N and  0 <= nx < N and visited[ny][nx] == -1:
                queue.append([ny, nx])
                visited[ny][nx] = visited[y][x] + 1

N = 4
pos = [[1,0],[-1,0],[0,1],[0,-1]]

visited = [[-1] * N for _ in range(N)]
queue = []
A = [[1, 1, 1, 0],
     [1, 1, 0, 2],
     [1, 0, 2 ,2],
     [0, 2, 2, 2]]

for i in range(N):
    for j in range(N):
        if A[i][j] == 1:
            queue.append([i, j])
            visited[i][j] = 0

result = BFS()
print(result)
# 좌측 상단과 우측 하단의 최소 값을 구하여라

