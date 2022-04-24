from collections import deque

F, S, G, U, D = map(int, input().split())

visited = [-1] * 1000001
visited[S] = 1
queue = deque()
queue.append(S)

result = -1

while queue:
    now = queue.popleft()

    cnt = visited[now]
    if now == G:
        result = cnt

    for dx in (U, -D):
        ny = dx + now
        if 0 < ny <= F and visited[ny] == -1:
            queue.append(ny)
            visited[ny] = cnt + 1


if result == -1:
    print('use the stairs')
else:
    print(result - 1)