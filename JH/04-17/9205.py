# 오류 : 꼭 편의점을 다 들려야 하는 줄 암

import sys
input = sys.stdin.readline

def go_festival(route):
    route = [[s_x, s_y]] + route + [[e_x, e_y]]
    for i in range(N+1):
        x = abs(route[i][0] - route[i + 1][0])
        y = abs(route[i][1] - route[i + 1][1])
        dist = x + y
        if dist > 1000:
            return 0
    return 1

def dfs(depth):
    if depth == N:
        res = go_festival(result)
        return res

    for i in range(N):
        if visited[i] == False:
            visited[i] = True
            result[depth] = conv[i][:]
            res = dfs(depth+1)
            if res == 1:
                return 1
            visited[i] = False
    return 0

T = int(input())
for tc in range(1, 1+T):
    N = int(input())
    s_x, s_y = map(int, input().split())
    conv = []
    for i in range(N):
        x, y = map(int, input().split())
        conv.append([x, y])
    e_x, e_y = map(int, input().split())
    visited = [0] * (N+1)
    result = [0] * N
    flag = 0

    final = dfs(0)
    if final == 1:
        print("happy")
    else:
        print("sad")