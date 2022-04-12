N, M, S = map(int, input().split())

# 인접행렬 만들기
adjM = [[0] * (N+1) for _ in range(N+1)]

for i in range(M):
    A, B = map(int, input().split())
    adjM[A][B] = 1
    adjM[B][A] = 1

visited = [0] * (N+1)
visited[S] = 1
result = []
result.append(S)

def dfs(s):
    for i in range( N+1):
        if adjM[s][i] == 1 and visited[i] == 0:
            visited[i] = 1
            result.append(i)
            dfs(i)
dfs(S)
print(*result)
visited = [0] * (N+1)
queue = []
result = []
result.append(S)
queue.append(S)
visited[S] = 1
def bfs(s):
    while queue:
        s = queue.pop(0)
        for i in range( N+1):
            if adjM[s][i] == 1 and visited[i] == 0:
                queue.append(i)
                result.append(i)
                visited[i] = 1
bfs(S)
print(*result)
