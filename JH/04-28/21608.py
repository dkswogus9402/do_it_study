N = int(input())
A = [[0] * N for _ in range(N)]
pos = [[1,0], [-1,0], [0,1], [0,-1]]
table = [0] * (N*N+1)

input_data = []
for _ in range(N**2):
    data = list(map(int, input().split()))
    input_data.append(data)
    key = data[0]
    value = data[1:]
    table[key] = value[:]

for data in input_data:
    target = data[0]
    love_friend = data[1:]
    max_love_cnt = -1 # 주의해야함
    seat_x = seat_y = 0
    max_seat = -1 # 주의해야함 0,0이 불가능 함
    '''
    현재 근처에 자리와 좋아하는 사람을 찾음
    '''
    for i in range(N):
        for j in range(N):
            if A[i][j] == 0:
                seat_cnt = 0
                love_cnt = 0
                y, x = i, j
                for dy, dx in pos:
                    ny = dy + y
                    nx = dx + x
                    if 0<=ny<N and 0<=nx<N:
                        if A[ny][nx] == 0:
                            seat_cnt += 1
                        if A[ny][nx] in love_friend:
                            love_cnt += 1
                '''
                주의 해야함 max 값이 0이면서 근처에 자리가 없을 때 했을 때 오류 발생
                주의에 빈칸 0개 좋아하는 사람 0명일 경우 seat_x와 seat_y가 제대로 설정되지 못함
                '''
                if max_love_cnt < love_cnt or (max_love_cnt == love_cnt and max_seat < seat_cnt):
                    max_love_cnt = love_cnt
                    max_seat = seat_cnt
                    seat_x = x
                    seat_y = y

    A[seat_y][seat_x] = target

total = 0
for i in range(N):
    for j in range(N):
        cnt = 0
        y, x = i, j
        love_friends = table[A[i][j]]
        for dy, dx in pos:
            ny = dy + y
            nx = dx + x
            if 0 <=ny< N and 0<=nx<N:
                if A[ny][nx] in love_friends:
                   cnt += 1

        if cnt == 0:
            total += 0
        elif cnt == 1:
            total += 1
        elif cnt == 2:
            total += 10
        elif cnt == 3:
            total += 100
        elif cnt == 4:
            total += 1000

print(total)