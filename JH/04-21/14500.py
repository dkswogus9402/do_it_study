N, M = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]

def add_func(i,j):
    global max_value

    y, x = i, j
    pos_candi = [[[0,1], [0,2], [1,1]], [[0,1], [0,2], [-1,1]], [[-1,1],[0,1],[1,1]], [[-1,-1],[0,-1],[1,-1]]]
    for pos in pos_candi:
        sum_data = A[y][x]
        for dy, dx in pos:
            ny, nx = dy + y, dx + x
            if 0<=ny<N and 0<=nx<M:
                sum_data += A[ny][nx]
            else:
                break
        else:
            if max_value < sum_data:
                max_value = sum_data


def DFS(i, j, depth, _sum):
    global max_value
    y, x = i, j

    if depth == 4:
        if max_value < _sum:
            max_value = _sum
        return

    for dy, dx in ((0,1), (0,-1), (1,0), (-1,0)):
        ny = dy + y
        nx = dx + x
        if 0<=ny<N and 0<=nx<M and visited[ny][nx] == 0:
            visited[ny][nx] = 1
            DFS(ny,nx,depth+1,_sum+A[ny][nx])
            visited[ny][nx] = 0

visited = [[0] * M for _ in range(N)]
max_value = 0
for i in range(N):
    for j in range(M):
        visited[i][j] = 1
        DFS(i, j, 1, A[i][j])
        visited[i][j] = 0
        add_func(i, j)

print(max_value)