from collections import deque

N, Q = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(2**N)]
L_list = list(map(int, input().split()))

for L in L_list:
    if L > 0:
        for i in range(0, 2**N, 2**L):
            for j in range(0, 2**N, 2**L):
                value = [A[k][j:j+2**L] for k in range(i, i+2**L)]
                value = list(zip(*value[::-1]))

                for y in range(2 ** L):
                    for x in range(2 ** L):
                        A[y + i][x + j] = value[y][x]

    temp = []
    pos = ((0,1),(0,-1),(1,0),(-1,0))
    for y in range(2**N):
        for x in range(2**N):
            if A[y][x] != 0:
                cnt = 0
                for dy, dx in pos:
                    ny, nx = dy + y, dx + x
                    if 0<=ny<2**N and 0<=nx<2**N and A[ny][nx] != 0:
                        cnt += 1
                if cnt < 3 :
                    temp.append([y,x])
    for y, x in temp:
        if A[y][x] > 0:
            A[y][x] -= 1

def BFS(i, j):
    queue = deque()
    queue.append([i, j])
    visited[i][j] = 1
    cnt = 1

    while queue:
        y, x = queue.popleft()

        for dy, dx in pos:
            ny, nx = dy + y, dx + x
            if 0<=ny< 2**N and 0<=nx< 2**N and A[ny][nx] != 0 and visited[ny][nx] == 0:
                queue.append([ny,nx])
                visited[ny][nx] = 1
                cnt += 1
    return cnt

visited = [[0] * 2**N for _ in range(2**N)]
max_value = lump =0
for i in range(2**N):
    for j in range(2**N):
        if A[i][j] != 0 and visited[i][j] == 0:
            lump = BFS(i, j)
        if max_value < lump:
            max_value = lump

result = 0
for i in range(2**N):
    result += sum(A[i])
print(result)
print(max_value)