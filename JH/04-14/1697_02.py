from collections import deque

A, B = map(int, input().split())
visited = [0] * 100001

queue = deque()
queue.append(A)
visited[A] = 1

while queue:
    x = queue.popleft()

    if x == B:
        print(visited[x]-1)

    for dx in (x, -1, 1):
        nx = dx + x
        if 0<=nx<100001 and visited[nx] == 0:
            queue.append(nx)
            visited[nx] = visited[x] + 1

