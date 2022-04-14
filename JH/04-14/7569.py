from collections import deque

def bfs():
    queue = deque()
    for h in range(H):
        for n in range(N):
            for m in range(M):
                if A[h][n][m] == 1:
                    queue.append([h, n, m])
                    visited[h][n][m] = 1

    while queue:
        z, y, x = queue.popleft()
        for dz, dy, dx in ((0, 0, 1), (0, 0, -1), (0, 1, 0), (0, -1, 0), (1, 0, 0), (-1, 0, 0)):
            nz = dz + z
            ny = dy + y
            nx = dx + x
            if 0 <= nz < H and 0 <= ny < N and 0 <= nx < M and A[nz][ny][nx] == 0:
                queue.append([nz, ny, nx])
                A[nz][ny][nx] = A[z][y][x] + 1

M, N, H = map(int, input().split())

A = []
for h in range(H):
    a = [list(map(int, input().split())) for _ in range(N)]
    A.append(a)

visited = [[[0]*M for _ in range(N)] for _ in range(H)]
bfs()
result = 0
max_value = 0
for h in range(H):
    for n in range(N):
        for m in range(M):
            if A[h][n][m] == 0:
                result = -1

            if max_value < A[h][n][m]:
                max_value = A[h][n][m]

if result == -1:
    print(-1)
else:
    print(max_value)