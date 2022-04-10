A = [[0,0,0,0,0],
    [0,1,0,0,0],
    [0,0,0,0,0],
    [0,0,0,0,0],
    [0,0,0,0,0]]

N = 5
pos = [[0,1], [0,-1], [1,0], [-1,0]]
visited = [[0] * N for _ in range(N)]

queue = []
queue.append([1,1])
visited[1][1] = 1

while queue:
    y, x = queue.pop(0)
    for dy, dx in pos:
        ny = dy + y
        nx = dx + x
        if 0 <= nx < N and 0 <= ny < N and visited[ny][nx] == 0:
            queue.append([ny, nx])
            visited[ny][nx] = visited[y][x] + 1

for i in visited:
    print(i)