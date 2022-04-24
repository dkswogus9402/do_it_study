from collections import deque

T = int(input())

for tc in range(1, 1+T):
    N = int(input())
    s_x, s_y = map(int, input().split())
    conven = []
    for _ in range(N):
        data = list(map(int, input().split()))
        conven.append(data)
    e_x, e_y = map(int, input().split())
    visited = [0] * N
    queue = deque()
    queue.append([s_x, s_y])
    flag = 0
    while queue:
        x, y = queue.popleft()

        if abs(x - e_x) + abs(y-e_y) <= 1000:
            flag = 1
            break

        for i in range(N):
            if visited[i] == 0 and abs(x - conven[i][0]) + abs(y-conven[i][1]) <= 1000:
                visited[i] = 1
                queue.append(conven[i])

    if flag == 1:
        print('happy')
    else:
        print('sad')
