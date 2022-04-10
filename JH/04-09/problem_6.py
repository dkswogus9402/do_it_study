def BFS(start, end):
     queue = []
     visited = [[0] * N for _ in range(N)]

     for i in range(N):
          for j in range(N):
               if A[i][j] == start:
                    queue.append([i, j])
                    visited[i][j] = 1

     while queue:
          y, x = queue.pop(0)

          if A[y][x] == end:
               return visited[y][x]

          for dy, dx in ((0, 1), (0, -1), (1, 0), (-1, 0)):
               ny = dy + y
               nx = dx + x
               if 0 <= ny < N and 0 <= nx < N and visited[ny][nx] == 0 and A[ny][nx] != 1:
                    queue.append([ny, nx])
                    visited[ny][nx] = visited[y][x] + 1


# 2에서 3이동
# 3에서 4이동 최소거리
pos = [[1,0], [-1,0], [0,1], [0,-1]]
N = 5
A = [[0, 2, 1, 1, 4],
     [0, 1, 0, 0, 0],
     [0, 0, 1, 1 ,0],
     [1, 0, 0, 0, 0],
     [1, 0, 1, 1, 3]]


c = BFS(2,3)
d = BFS(3,4)
print(c+d)