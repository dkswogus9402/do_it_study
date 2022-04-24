dy = [-1,-1,0,1,1,1, 0, -1]
dx = [0,1,1,1,0,-1,-1,-1]


N, M, K = map(int, input().split())
A = [[[] for _ in range(N)] for _ in range(N)]
for _ in range(M):
    r,c,m,s,d = map(int, input().split())
    A[r-1][c-1].append([m,s,d])

for _ in range(K):
    temp = []
    for i in range(N):
        for j in range(N):
            y, x = i, j
            if A[i][j] != []:
                while A[i][j]:
                    m, s, d = A[i][j].pop()
                    ny = y + (dy[d] * s)
                    nx = x + (dx[d] * s)
                    if ny < 0:
                        ny = (ny%N)
                    elif ny > N-1:
                        ny = (ny%N)
                    if nx < 0:
                        nx = (nx%N)
                    elif nx > N-1:
                        nx = (nx%N)
                    temp.append([ny,nx,m,s,d])
    while temp:
        y,x,m,s,d = temp.pop()
        A[y][x].append([m,s,d])

    for i in range(N):
        for j in range(N):
            y, x = i, j
            if len(A[i][j]) != 1:
                total_m = 0
                total_s = 0
                check_d = []
                len_target = len(A[i][j])
                while A[i][j]:
                    m, s, d = A[i][j].pop()
                    total_m += m
                    if d % 2 == 0:
                        check_d.append(0)
                    else:
                        check_d.append(1)
                    total_s += s
                # 4개로 갈라짐
                if len(set(check_d)) == 1:
                    pos = [0, 2, 4, 6]
                else:
                    pos = [1, 3, 5, 7]

                if total_m // 5 == 0:
                    continue
                n_m = total_m // 5
                n_s = total_s // len_target
                for d in pos:
                    temp.append([y, x, n_m, n_s, d])
    while temp:
        y, x, m, s, d = temp.pop()
        A[y][x].append([m, s, d])

result = 0
for i in range(N):
    for j in range(N):
        if A[i][j] != []:
            for m, s, d in A[i][j]:
                result += m
print(result)