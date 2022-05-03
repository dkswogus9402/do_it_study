from collections import deque

N, Q = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(2**N)]

L_list = list(map(int, input().split()))

for L in L_list:
    if L > 0:
        for i in range(0, 2 ** N, 2 ** L):
            for j in range(0, 2 ** N, 2 ** L):
                value = [A[k][j:(j + 2 ** L)] for k in range(i, (i + 2 ** L))]
                value = list(zip(*value[::-1]))
                for y in range(2 ** L):
                    for x in range(2 ** L):
                        A[i + y][j + x] = value[y][x]

    temp = []
    for i in range(2**N):
        for j in range(2**N):
            flag = 0
            if A[i][j] != 0:
                for dy, dx in ((0,1),(0,-1),(1,0),(-1,0)):
                    ny = dy + i
                    nx = dx + j
                    if 0<=ny< 2**N and 0<=nx< 2**N and A[ny][nx] != 0:
                        flag += 1
                if flag < 3:
                    temp.append([i, j])
    for y, x in temp:
        A[y][x] -= 1

def BFS(i,j):
    queue = deque()
    queue.append([i,j])
    visited[i][j] = 1
    cnt = 1

    while queue:
        y, x = queue.popleft()

        for dy, dx in ((0, 1), (0, -1), (1, 0), (-1, 0)):
            ny = dy + y
            nx = dx + x
            if 0<=ny<2**N and 0<=nx<2**N and A[ny][nx] != 0 and visited[ny][nx] == 0:
                queue.append([ny,nx])
                visited[ny][nx] = 1
                cnt += 1
    return cnt

max_value = 0
total = 0
visited = [[0] * (2**N) for _ in range(2**N)]
for i in range(2**N):
    for j in range(2**N):
        total += A[i][j]
        if A[i][j] != 0 and visited[i][j] == 0:
            result = BFS(i,j)
            if max_value < result:
                max_value = result

print(total)
print(max_value)