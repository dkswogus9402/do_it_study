N = int(input())
A, B = map(int, input().split())
M = int(input())

adjM = [[0] * (N+1) for _ in range(N+1)]

for _ in range(M):
    a, b = map(int, input().split())
    adjM[a][b] = 1
    adjM[b][a] = 1

visited = [0] * (N+1)

def dfs(num, cnt):
    global result
    global min_value

    if num == B:
        if cnt < min_value:
            min_value = cnt
        return

    if min_value <= cnt:
        return

    for i in range(N+1):
        if visited[i] == 0 and adjM[num][i] == 1:
            visited[i] = 1
            dfs(i, cnt + 1)
            visited[i] = 0

min_value = 100000
visited[A] = 1
dfs(A, 0)
result = -1 if min_value == 100000 else min_value
print(result)
