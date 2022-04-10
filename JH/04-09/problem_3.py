N = 4
pos = [[1,0],[-1,0],[0,1],[0,-1]]

A = [[1, 1, 1, 1],
     [1, 1, 0, 2],
     [1, 0, 2 ,2],
     [0, 2, 2, 2]]

# 1의 크기 2의 크기

visited = [[0] * N for _ in range(N)]
queue = []
queue.append([0,0])
visited[0][0] = 1
queue.append([N-1,N-1])
visited[N-1][N-1] = 1

cnt_1 = cnt_2 = 0
while queue:
    y, x = queue.pop(0)
    if A[y][x] == 1:
        cnt_1 += 1
    elif A[y][x] == 2:
        cnt_2 += 1

    for dy, dx in pos:
        ny = dy + y
        nx = dx + x
        if 0<=ny<N and 0<=nx<N and visited[ny][nx] == 0 and A[ny][nx] != 0:
            queue.append([ny, nx])
            visited[ny][nx] = 1

for i in visited:
    print(i)
print(cnt_1, cnt_2)