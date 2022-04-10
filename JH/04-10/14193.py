from collections import deque

# BFS 여러 가지 출발점을 가진 BFS + BFS 섬 사이의 최소 거리

def BFS(i, j):
    global cnt

    queue = []
    queue.append([i, j])

    while True:
        bfs_queue = deque()
        flag = 0
        visited = [[-1] * M for _ in range(N)]
        for y, x in queue:
            bfs_queue.append([y,x])
            visited[y][x] = 0

        while bfs_queue:
            y, x = bfs_queue.popleft()

            if ground[y][x] == 'A' and visited[y][x] != 0:
                cnt += visited[y][x]
                queue.append([y,x])
                flag = 1
                break

            for dy, dx in ((0, -1), (0, 1), (1, 0), (-1, 0)):
                ny = dy + y
                nx = dx + x
                if 0 <= ny < N and 0 <= nx < M and visited[ny][nx] == -1 and ground[ny][nx] != '#':
                    bfs_queue.append([ny, nx])
                    visited[ny][nx] = visited[y][x] + 1

        if not bfs_queue and flag != 1: # 더이상 찾을 것이 없다.
            break

T = int(input())
for tc in range(1, 1+T):
    M, N = map(int, input().split())
    ground = [list(input()) for _ in range(N)]
    cnt = 0
    for i in range(N):
        for j in range(M):
            if ground[i][j] == 'S':
                BFS(i,j)
    print(cnt)
