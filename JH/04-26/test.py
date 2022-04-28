N, M = 7, 1
A = [[1, 1, 1, 1, 1, 2, 1],
    [3, 2, 1, 3, 2, 3, 1],
    [2, 1, 2, 1, 2, 1, 3],
    [2, 1, 1, 0, 1, 2, 3],
    [3, 3, 2, 3, 2, 1, 2],
    [3, 1, 3, 1, 3, 3, 2],
    [2, 3, 2, 2, 3, 2, 3]]
ds_list = [list(map(int, input().split())) for _ in range(M)]

 # 상어는 항상 제자리네

pos = ((-1,0),(1,0),(-1,0),(0,1))
result = [0] * 4
def blizzard(d, s):
    y, x = N // 2, N // 2
    # 방향
    for i in range(1,s+1):
        ny = y + (pos[d - 1][0] * i)
        nx = x + (pos[d - 1][1] * i)
        A[ny][nx] = 0 # 우선 0이라고 표현


def reshape(A): # 뽑아내는 과정
    y, x = N//2, N//2
    cnt = 0
    direction = 0
    move = ((0,-1),(1,0),(0,1),(-1,0))
    flag = False
    temp = [] # reshape 하기위한 변수
    while True:
        if direction % 2 == 0:
            cnt += 1
        if cnt == N:
            cnt -= 1
            flag = True
        for _ in range(cnt):
            y = y + move[direction][0]
            x = x + move[direction][1]
            if A[y][x]: # 0인 것을 제외하고 데이터를 가져옴
                temp.append(A[y][x])
        direction = (direction + 1 ) % 4
        if flag:
            break
    # Temp embedding 과정
    # temp = temp + ([0] * (N * N - len(temp))) # 한개는 상어위치
    return temp

def reshape_2(temp):    # 채워주는 과정
    A = [[0] * N for _ in range(N)]
    y, x = N//2, N//2
    cnt = 0
    direction = 0
    k = 0
    move = ((0,-1),(1,0),(0,1),(-1,0))
    flag = False
    while True:
        if direction % 2 == 0:
            cnt += 1
        if cnt == N:
            cnt -= 1
            flag = True
        for _ in range(cnt):
            y = y + move[direction][0]
            x = x + move[direction][1]
            A[y][x] = temp[k]
            k += 1
        direction = (direction + 1 ) % 4
        if flag:
            break
    return A

def boob(temp):
    global result

    cnt = 1
    what_cnt = 1
    flag = 0
    while flag != 1:
        for i in range(len(temp)-1): # 제일 마지막 경우 체크 한번 더
            if temp[i] == 0 or i == len(temp)-2:
                what_cnt = cnt
                print(what_cnt)
                if what_cnt > 3:
                    for _ in range(what_cnt+1):
                        temp.pop()
                flag = 1
                break
            if temp[i] == temp[i+1]:
                cnt += 1
            else:
                what_cnt = cnt
                cnt = 1
            if what_cnt > 3:
                result[temp[i]] += what_cnt
                for k in range(what_cnt):
                    temp.pop(i-k)
                what_cnt = 0
                break
    print(temp)
    print(len(temp))
    # 구술이 폭발하고 이동한 후
    new_temp = []
    cnt = 1
    for i in range(len(temp) - 1):  # 제일 마지막 경우 체크 한번 더
        if temp[i] == temp[i + 1]:
            cnt += 1
        else:
            what_cnt = cnt
            cnt = 1
            new_temp.append(what_cnt)
            new_temp.append(temp[i])
    new_temp = new_temp + ([0] * (N * N - len(new_temp))) # 한개는 상어위치
    # print(len(new_temp))

    return new_temp


for d, s in ds_list:
    blizzard(d, s)
    temp = reshape(A)
    new_temp = boob(temp)
    A = reshape_2(new_temp)
total = result[1] + 2 * result[2] + 3 * result[3]
print(total)