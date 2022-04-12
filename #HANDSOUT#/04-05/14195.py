
def BFS(i, j):
    global max_value
    global cnt_1, cnt_2

    queue = []
    queue.append([i, j])
    visited[i][j] = 1
    cnt = 1
    while queue:
        y, x = queue.pop(0)
        for dy, dx in ((1,0),(-1,0),(0,-1),(0,1)):
            ny = dy + y
            nx = dx + x
            if 0 <= ny < N and 0 <= nx < M and visited[ny][nx] == 0 and A[i][j] == A[ny][nx]:
                queue.append([ny, nx])
                visited[ny][nx] = 1
                cnt += 1

    if A[i][j] == 'A':
        cnt_1 += 1

    elif A[i][j] == 'B':
        cnt_2 += 1

    if max_value < cnt:
        max_value = cnt
    return

T = int(input())
for tc in range(1, 1+T):
    N, M = map(int, input().split())
    A = [list(input()) for _ in range(N)]
    visited = [[0] * M for _ in range(N)]
    what_cnt = 0
    max_value = 0
    cnt_1 = cnt_2 = 0

    for i in range(N):
        for j in range(M):
            if A[i][j] != '_' and visited[i][j] == 0:
                BFS(i, j)

    print('#{} {} {} {}'.format(tc, cnt_1, cnt_2, max_value))