from collections import deque

def BFS(i, j):
    queue = deque()
    visited = [[0] * M for _ in range(N)]

    queue.append([i,j])
    visited[i][j] = 1

    while queue:
        y, x = queue.popleft()

        life_flower[visited[y][x]] += 1 # BFS에서 생명주기 리스트 생성
        life_flower[visited[y][x] + A[y][x]] -= 1

        for dy, dx in ((0,1), (0,-1), (1, 0), (-1,0)):
            ny = dy + y
            nx = dx + x
            if 0 <=ny< N and 0 <= nx < M and visited[ny][nx] == 0 and A[ny][nx] != 0:
                queue.append([ny,nx])
                visited[ny][nx] = visited[y][x] + 1


T = int(input())

for tc in range(1, 1+T):
    N, M = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(N)]

    s_x, s_y = map(int, input().split())

    life_flower = [0] * 1001001

    BFS(s_y, s_x)
    max_value = 0
    max_day = 0

    for i in range(1, N*M): # 최고 값 구하기 memoization
        life_flower[i] = life_flower[i-1] + life_flower[i]

        if max_value < life_flower[i]:
            max_value = life_flower[i]
            max_day = i

    print('#{} {}일 {}개'.format(tc, max_day, max_value))