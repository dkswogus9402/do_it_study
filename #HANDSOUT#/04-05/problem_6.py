def BFS(start, end):
    visited = [[-1] * N for _ in range(N)]
    queue = []
    for i in range(N):
        for j in range(N):
            if A[i][j] == start:
                queue.append([i, j])
                visited[i][j] = 0
                break
    result = 0
    while queue:
        y, x = queue.pop(0)
        if A[y][x] == end:
            result = visited[y][x]
            break

        for dy, dx in pos:
            ny = dy + y
            nx = dx + x
            if 0 <= ny < N and 0 <= nx < N and visited[ny][nx] == -1 and A[ny][nx] != 1:
                queue.append([ny, nx])
                visited[ny][nx] = visited[y][x] + 1
    return result

pos = [[1,0], [-1,0], [0,1], [0,-1]]
N = 5
A = [[0, 2, 1, 1, 4],
     [0, 1, 0, 0, 0],
     [0, 0, 1, 1 ,0],
     [1, 0, 0, 0, 0],
     [1, 0, 1, 1, 3]]

cnt_1 = BFS(2, 3)
cnt_2 = BFS(3, 4)
result = cnt_1 + cnt_2
print(result)