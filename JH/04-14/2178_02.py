from collections import deque

N, M = map(int, input().split())

A = [list(map(int, input())) for _ in range(N)]
visited = [[0] * M for _ in range(N)]

def bfs(s_y, s_x):
    visited[s_y][s_x] = 1
    queue = deque()
    queue.append([s_y, s_x])

    while queue:
        y, x = queue.popleft()

        if y == N-1 and x == M-1:
            print(visited[y][x])
            return

        for dy, dx in ((0,1),(0,-1),(1,0),(-1,0)):
            ny = dy + y
            nx = dx + x
            if 0 <= ny < N and 0 <= nx < M:
                if visited[ny][nx] != 0:
                    continue

                if A[ny][nx] != 1:
                    continue

                queue.append([ny,nx])
                visited[ny][nx] = visited[y][x] + 1
    return


bfs(0,0)