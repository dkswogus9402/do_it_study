from collections import deque

N = int(input())
A, B = map(int, input().split())

adjM = [[0] * (N+1) for _ in range(N+1)]

M = int(input())
for _ in range(M):
    a, b = map(int, input().split())
    adjM[a][b] = 1
    adjM[b][a] = 1

visited = [0] * (N+1)
queue = deque()
queue.append(A)
visited[A] = 1

result = -1

while queue:
    num = queue.popleft()

    if num == B:
        result = visited[num] -1

    for i in range(N+1):
        if visited[i] == 0 and adjM[num][i] == 1:
            queue.append(i)
            visited[i] = visited[num] + 1

print(result)