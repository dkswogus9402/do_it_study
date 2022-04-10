# 벽 두개를 부수고 연구소
depth = 2
N = 5
pos = [[1,0],[-1,0],[0,1],[0,-1]]

A = [[2, 1, 1, 1, 0],
     [0, 1, 0, 0, 1],
     [0, 1, 1 ,1, 0],
     [1, 0, 1, 1, 0],
     [1, 0, 1, 1, 3]]

visited = [[[-1] * N for _ in range(N)] for _ in range(depth+1)]

queue = []
queue.append([0,0,0])
visited[0][0][0] = 0

while queue:
     cnt, y, x = queue.pop(0)
     if A[y][x] == 3 and cnt == 2 :
          print(visited[cnt][y][x])

     for dy, dx in pos:
          ny = dy + y
          nx = dx + x
          if 0<= ny < N and 0<= nx < N and cnt <= 2 and visited[cnt][ny][nx] == -1:
               n_cnt = cnt
               if A[ny][nx] == 1:
                    if cnt == 2:
                         continue
                    n_cnt += 1
               queue.append([n_cnt, ny, nx])
               visited[n_cnt][ny][nx] = visited[cnt][y][x] + 1
