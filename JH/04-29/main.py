N = int(input())
input_lists = []
table = [0] * (N*N+1)
for _ in range(N*N):
    data = list(map(int, input().split()))
    input_lists.append(data)
    key = data[0]
    value = data[1:]
    table[key] = value

A = [[0] * N for _ in range(N)]

pos = ((1,0),(-1,0),(0,1),(0,-1))
for input_list in input_lists:
    student = input_list[0]
    love_friends = input_list[1:]
    max_love = -1 # 빈칸이라도 들어갈 수 있도록 수정
    max_seat = 0
    for i in range(N):
        for j in range(N):
            seat = 0
            love = 0
            if A[i][j] == 0: # 자리가 비어있다면, 해당 자리 근처에 빈칸 갯수와 좋아하는 사람 개수
                y, x = i, j
                for dy, dx in pos:
                    ny = dy + y
                    nx = dx + x
                    if 0 <= ny < N and 0 <= nx < N:
                        if A[ny][nx] == 0:
                            seat += 1

                        elif A[ny][nx] in love_friends:
                            love += 1

                if max_love < love or (max_love == love and max_seat < seat):
                    max_love = love
                    max_seat = seat
                    res_y = y
                    res_x = x
    A[res_y][res_x] = student


result = 0
for i in range(N):
    for j in range(N):
        love_friend = table[A[i][j]]
        cnt = 0
        for dy, dx in pos:
            ny = dy + i
            nx = dx + j
            if 0 <= ny < N and 0<= nx < N and A[ny][nx] in love_friend:
                cnt += 1
        if cnt == 0:
            result += 0
        elif cnt == 1:
            result += 1
        elif cnt == 2:
            result += 10
        elif cnt == 3:
            result += 100
        elif cnt == 4:
            result += 1000

print(result )