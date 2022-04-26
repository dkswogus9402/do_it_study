N, M = map(int, input().split())
A = [ list(map(int, input().split())) for _ in range(N)]


pos = ((0,-1),(-1,-1),(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1))

def move_cloud(cloud, d, s):
    # 이동
    visited = [[0] * N for _ in range(N)]
    new_cloud = []
    for y, x in cloud:
        ny = (y + (pos[d-1][0] * s)) % N
        nx = (x + (pos[d-1][1] * s)) % N
        A[ny][nx] += 1
        visited[ny][nx] = 1
        new_cloud.append((ny,nx))

    for y, x in new_cloud:
        r_pos = ((1,1),(-1,-1),(1,-1),(-1,1))
        for dy, dx in r_pos:
            n_y = y + dy
            n_x = x + dx
            if 0 <= n_y < N and 0 <= n_x < N and A[n_y][n_x] != 0:
                A[y][x] += 1
    temp = []
    for i in range(N):
        for j in range(N):
            if A[i][j] >= 2 and visited[i][j] == 0:
                A[i][j] -= 2
                temp.append([i,j])
    return temp

cloud = ((N-1, 0), (N-1, 1), (N-2, 0), (N-2, 1))
for _ in range(M):
    d, s = map(int, input().split())
    cloud = move_cloud(cloud, d, s)
total = 0
for i in range(N):
    total += sum(A[i])
print(total)