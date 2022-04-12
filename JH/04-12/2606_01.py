N = int(input())
M = int(input())

adjM = [[0]*(N+1) for _ in range(N+1)]

for _ in range(M):
    A, B = map(int, input().split())
    adjM[A][B] = 1
    adjM[B][A] = 1

visited = [0] * (N+1)
s = 1
visited[s] = 1
result = [s]
def dfs(s):

    for i in range(N+1):
        if visited[i] == 0 and adjM[s][i] == 1:
            visited[i] = 1
            result.append(i)
            dfs(i)
dfs(s)
print(len(result)-1)