N = int(input())
A = list(map(int, input().split()))
visited = list(map(int, input().split()))

res = sum(visited)
result = A[0]
max_value = -1000000001
min_value = 1000000001

def dfs(depth, visited, result):
    global max_value, min_value

    if depth == res:
        if max_value < result:
            max_value = result

        if min_value > result:
            min_value = result
        return

    for i in range(4):
        if visited[i] != 0:
            visited[i] -= 1
            if i == 0:
                dfs(depth + 1, visited, result + A[depth + 1])
            elif i == 1:
                dfs(depth + 1, visited, result - A[depth + 1])
            elif i == 2:
                dfs(depth + 1, visited, result * A[depth + 1])
            else:
                flag = 1
                if result < 0 and A[depth+1] < 0:
                    flag = 1
                elif result < 0:
                    flag = -1
                elif A[depth+1] < 0:
                    flag = -1
                dfs(depth + 1, visited, abs(result) // abs(A[depth + 1]) * flag )
            visited[i] += 1

dfs(0, visited, A[0])
print(max_value)
print(min_value)