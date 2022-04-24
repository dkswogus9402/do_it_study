# 생각보다 난관이였음 - > x와 y의 위치오류
# 반드시 2개를 주어진 편의점을 다 돌 필요는 없음

from collections import deque

def BFS(s_y, s_x, conv, e_x, e_y):
    queue = deque()
    queue.append([s_x, s_y])
    visited = [0] * N
    while queue:
        x, y = queue.popleft()

        if abs(y - e_y) + abs(x - e_x) <= 1000:
            print('happy')
            return

        for i in range(N):
            if visited[i] == 0:
                d_x, d_y = conv[i]
                if abs(y - d_y) + abs(x - d_x) <= 1000:
                    queue.append([d_x, d_y])
                    visited[i] = 1
    print('sad')


T = int(input())
for tc in range(1, 1+T):
    N = int(input())
    s_x, s_y = map(int, input().split())
    conv = []
    for i in range(N):
        x, y = map(int, input().split())
        conv.append([x, y])
    e_x, e_y = map(int, input().split())

    BFS(s_y, s_x, conv, e_x, e_y)