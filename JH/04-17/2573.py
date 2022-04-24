# python 시간초과 pypy 해결

import sys
from collections import deque
input = sys.stdin.readline

def BFS(i,j):
    queue = deque()
    queue.append([i,j])
    visited[i][j] = 1

    while queue:
        y, x = queue.popleft()
        for dy, dx in ((1,0), (-1,0), (0,1),(0,-1)):
            ny, nx = dy + y, dx + x
            if 0 <= ny < N and 0 <= nx < M and visited[ny][nx] == 0:
                if A[ny][nx] == 0:
                    continue
                queue.append([ny,nx])
                visited[ny][nx] = 1


N, M = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]


def ice_melts():
    candidate = []
    for i in range(N):
        for j in range(M):
            if A[i][j] == 0:
                candidate.append([i, j])

    for y, x in candidate:
        for dy, dx in ((0,1),(0,-1), (1,0), (-1,0)):
            ny = dy + y
            nx = dx + x
            if 0 <= ny < N and 0 <= nx < M and A[ny][nx] > 0:
                A[ny][nx] -= 1

result = 0
for k in range(100000):
    if k != 0:
        ice_melts()

    visited = [[0] * M for _ in range(N)]
    cnt = 0

    for i in range(N):
        for j in range(M):
            if A[i][j] != 0 and visited[i][j] == 0:
                cnt += 1
                BFS(i, j)

    if 2 <= cnt:
        result = k
        break

    if cnt == 0:
        break

print(result)