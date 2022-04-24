from collections import deque
N, M = map(int, input().split())

A = [list(map(int, input().split())) for _ in range(N)]


def fuzing():
    candi = []
    for i in range(N):
        for j in range(M):
            if A[i][j] != 0:
                cnt = 0
                for dy, dx in ((1,0), (-1,0), (0,1), (0,-1)):
                    ny = dy + i
                    nx = dx + j
                    if A[ny][nx] == 0:
                        cnt += 1
                candi.append([i, j, cnt])

    for i in range(len(candi)):
        y, x, cnt = candi[i]
        A[y][x] -= cnt
        if A[y][x] < 0:
            A[y][x] = 0

def BFS(i,j):
    queue = deque()
    queue.append([i,j])
    visited[i][j] = 1

    while queue:
        y, x = queue.popleft()

        for dy, dx in ((0,1),(0,-1),(1,0),(-1,0)):
            ny = dy + y
            nx = dx + x
            if 0 <= ny < N and 0<= nx < M and visited[ny][nx] == 0 and A[ny][nx] > 0:
                queue.append([ny,nx])
                visited[ny][nx] = 1


time = 0
while True:

    time += 1
    fuzing()

    cnt = 0
    visited = [[0] * M for _ in range(N)]
    for i in range(N):
        for j in range(M):
            if A[i][j] != 0 and visited[i][j] == 0:
                cnt += 1
                BFS(i,j)

    if cnt >= 2:
        print(time)
        break

    if cnt == 0:
        print(0)
        break
