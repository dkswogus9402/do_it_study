N, M, S = map(int, input().split())
# 인접행렬 만들기
adjM = [[0] * (N+1) for _ in range(N+1)]

for i in range(M):
    A, B = map(int, input().split())
    adjM[A][B] = 1
    adjM[B][A] = 1

visited = [0] * (N+1)
visited[S] = 1
result = [S]

def dfs(s):
    for i in range(N+1): # 이 부분 실수
        if adjM[s][i] == 1 and visited[i] == 0:
            visited[i] = 1
            result.append(i)
            dfs(i)

dfs(S)
print(result)

visited = [0] * (N+1)
visited[S] = 1
result = [S]
queue = [S]
def BFS():
    while queue:
        s = queue.pop()
        for i in range(N+1): # 이 부분 실수
            if visited[i] == 0 and adjM[s][i] == 1:
                queue.append(i)
                result.append(i)
                visited[i] = 1

BFS()
print(result)