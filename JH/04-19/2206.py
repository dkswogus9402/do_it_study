from collections import deque

N,M = map(int, input().split())
A = [list(map(int, input())) for _ in range(N)]

visited = [[[0] * M for _ in range(N)] for _ in range(2)]

s_y, s_x = 0, 0
cnt = 0
queue = deque()
queue.append([cnt, s_y, s_x])
visited[cnt][s_y][s_x] = 1

result = -1
while queue:
    cnt,y, x = queue.popleft()

    if y == N-1 and x == M-1:
        result = visited[cnt][y][x]
        break

    for dy, dx in ((0,1),(0,-1),(1,0),(-1,0)):
        ny = dy + y
        nx = dx + x
        n_cnt = cnt
        if 0<= ny < N and 0<=nx < M:
            if A[ny][nx] == 1:
                n_cnt += 1
                if n_cnt == 2:
                    continue

            if visited[n_cnt][ny][nx] == 0:
                visited[n_cnt][ny][nx] = visited[cnt][y][x] + 1
                queue.append([n_cnt, ny, nx])
print(result)