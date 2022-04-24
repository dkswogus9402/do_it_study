from collections import deque

N, K = map(int, input().split())
visited = [0] * 100001


queue = deque()
queue.append(N)
visited[N] = 1

while queue:
    x = queue.popleft()

    if x == K:
        print(visited[x] - 1)
        break

    for dx in (x, -1, +1):
        nx = dx + x
        if 0<=nx<100001 and visited[nx] == 0:
            queue.append(nx)
            visited[nx] = visited[x] + 1