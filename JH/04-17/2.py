def DFS(y, x, k):
    global min_value

    if A[y][x] == 3:
        min_value = k
        return

    for dy, dx in ((0,1),(0,-1),(1, 0),(-1, 0)): # 좌우 찾기
        if (dy == 1 and dx == 0) or (dy == -1 and dx == 0):
            for i in range(1, k+1):
                ny = (dy * i) + y
                nx = (dx * i) + x
                if 0 <=ny <N and 0 <= nx <M and visited[ny][nx] == 0:
                    if A[ny][nx] != 0:
                        visited[ny][nx] = 1
                        DFS(ny, nx, k)
                        visited[ny][nx] = 0
        else:
            ny = dy + y
            nx = dx + x
            if 0 <= ny < N and 0 <= nx < M and visited[ny][nx] == 0:
                if A[ny][nx] != 0:
                    visited[ny][nx] = 1
                    DFS(ny, nx, k)
                    visited[ny][nx] = 0



T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(N)]
    min_value = 1000000
    for k in range(1, 100):
        print(k)
        visited = [[0] * M for _ in range(N)]
        s_y, s_x = N-1, 0
        visited[s_y][s_x] = 1
        DFS(s_y, s_x, k)
        if min_value != 1000000:
            break
    print('#{} {}'.format(tc, min_value))


