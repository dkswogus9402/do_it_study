N, M = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]

ds_list =  [list(map(int, input().split())) for _ in range(M)]
pos = ((0,0),(-1,0),(1,0),(0,-1),(0,1))
result = [0] * 4
'''
블리자드가내려옴
'''
def blizzard(d, s, A):
    y = x = N//2
    for i in range(1, s+1):
        ny = y + (pos[d][0] * i)
        nx = x + (pos[d][1] * i)
        A[ny][nx] = 0

'''
달팽이모양으로 돌기
'''
def reshape(A):
    y = x = N // 2
    cnt = 0
    distance = 0
    move_pos = ((0,-1), (1,0), (0,1), (-1,0))
    flag = 0
    temp = []
    while True:
        if distance % 2 == 0:
            cnt += 1
        if cnt == N:
            cnt -= 1
            flag = 1

        for _ in range(cnt):
            y = y + move_pos[distance][0]
            x = x + move_pos[distance][1]
            if A[y][x] != 0:
                temp.append(A[y][x])
        distance = (distance + 1) % 4
        if flag == 1:
            break
    return temp

'''
폭탄 터트리기 -> 0인 것은 제외하고 달팽이 모양으로 가져옴
'''
def boom(temp):
    cnt = 1
    flag = 1
    while flag != 0:
        flag = 0
        for i in range(len(temp)-1):
            if i == len(temp)-2:
                if temp[i] == temp[i + 1]:
                    cnt += 1
                    if cnt > 3:
                        flag += 1
                        result[temp[i]] += cnt
                        for kk in range(cnt):
                            temp[i+1 - kk] = 0
                else:
                    if cnt > 3:
                        flag += 1
                        result[temp[i]] += cnt
                        for kk in range(cnt):
                            temp[i - kk] = 0
                cnt = 1 # 조심
                break

            if temp[i] == temp[i+1]:
                cnt += 1
            else:
                if cnt > 3:
                    result[temp[i]] += cnt
                    flag += 1
                    for k in range(cnt):
                        temp[i-k] = 0
                cnt = 1

        new_temp = []
        for j in range(len(temp)):
            if temp[j] != 0:
                new_temp.append(temp[j])
        temp = new_temp
    return temp

'''
가져온 달팽이 모양을 재 정의함(갯수, 구슬)
'''
def reshape2(temp):
    cnt = 1
    new_temp = []
    for i in range(len(temp) - 1):
        if i == len(temp) - 2:
            if temp[i] == temp[i + 1]:
                cnt += 1
            new_temp.append(cnt)
            new_temp.append(temp[i])

            if temp[i] != temp[i + 1]:
                new_temp.append(1)
                new_temp.append(temp[i+1])
            break

        if temp[i] == temp[i + 1]:
            cnt += 1
        else:
            new_temp.append(cnt)
            new_temp.append(temp[i])
            cnt = 1
    new_temp = new_temp + [0] * (N**2 - len(new_temp)-1)
    return new_temp

'''
달팽이 모양으로 데이터를 채워넣음
'''
def pull_data(temp):
    A = [[0] * N for _ in range(N)]
    y = x = N // 2
    cnt = 0
    distance = 0
    move_pos = ((0, -1), (1, 0), (0, 1), (-1, 0))
    flag = 0
    kkk = 0
    while True:
        if distance % 2 == 0:
            cnt += 1

        if cnt == N:
            cnt -= 1
            flag = 1

        for _ in range(cnt):
            y = y + move_pos[distance][0]
            x = x + move_pos[distance][1]
            A[y][x] = temp[kkk]
            kkk += 1
        distance = (distance + 1) % 4
        if flag == 1:
            break
    return A
for d, s in ds_list:
    blizzard(d, s, A)
    temp = reshape(A)
    if temp == []:
        break
    temp = boom(temp)
    temp = reshape2(temp)
    A = pull_data(temp)

total = result[1] + 2 * result[2] + 3*result[3]
print(total)