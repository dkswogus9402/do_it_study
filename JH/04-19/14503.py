N, M = map(int, input().split())
y, x, d = map(int, input().split())

A = [list(map(int, input().split())) for _ in range(N)]
visited = [[0] * M for _ in range(N)]
dy = [-1,0,1,0]
dx = [0,1,0,-1]
visited[y][x] = 1

def DFS(y,x,d):
    for _ in range(4):
        nd = (d + 3) % 4
        nx = x + dx[nd]
        ny = y + dy[nd]

        if A[ny][nx] == 0 and visited[ny][nx] == 0:
            visited[ny][nx] = 1
            DFS(ny, nx, nd)
            return
        d = nd

    nd = (d+2)%4
    ny = y + dy[nd]
    nx = x + dx[nd]
    if A[ny][nx] == 1:
        return
    else:
        DFS(ny,nx,d) # 방향 그대로 한칸 뒤로 감

DFS(y,x,d)
cnt = 0
for i in range(N):
    for j in range(M):
        if visited[i][j] == 1:
            cnt += 1

print(cnt)