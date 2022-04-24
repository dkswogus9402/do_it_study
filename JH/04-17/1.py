def dfs(i, j, depth, sum_value):
    global max_value

    if depth == 4:
        final_value = sum_value ** 2
        if max_value < final_value:
            max_value = final_value
        return

    y, x = i, j

    if x % 2 == 0:
        pos = [[-1,1], [-1,-1], [0,1], [0,-1], [-1,0], [1,0]]
    else:
        pos = [[1,-1], [1,1], [0,-1], [0,1], [1,0], [-1,0]]

    for dy, dx in pos:
        ny = dy + y
        nx = dx + x
        if 0 <= ny < N and 0 <= nx < M and visited[ny][nx] == 0:
            visited[ny][nx] = 1
            dfs(ny, nx, depth+1, sum_value + A[ny][nx])
            visited[ny][nx] = 0


def add_function(i, j):
    global max_value

    y, x = i, j
    if x % 2 == 0:
        pos = [[[-1,-1], [-1,1], [1,0]] , [[-1,0], [0,-1], [0,1]]]
    else:
        pos = [[[1, 1], [1, -1], [-1, 0]], [[1, 0], [0, 1], [0, -1]]]
    for p in pos:
        result = [A[y][x]]

        for dy, dx in p:
            ny = dy + y
            nx = dx + x
            if 0<= ny < N and 0<= nx < M:
                result.append(A[ny][nx])

        if len(result) == 4:
            final_value = sum(result) ** 2
            if max_value < final_value:
                max_value = final_value



T = int(input())
for tc in range(1, 1+T):
    M, N = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(N)]

    max_value = 0
    for i in range(N):
        for j in range(M):
            visited = [[0] * M for _ in range(N)]
            visited[i][j] = 1
            dfs(i, j, 1, A[i][j])
            add_function(i, j)

    print('#{} {}'.format(tc, max_value))


