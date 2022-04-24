N = int(input())
A = [list(map(int, input().split())) for _ in range(N)]

left = [[1,-1,0.1], [-1,-1,0.1], [1,0,0.07], [-1,0,0.07],
            [-1,1,0.01], [1,1,0.01], [-2,0,0.02],[2,0,0.02],
            [0,-2,0.05], [0,-1,0]]
right = [(y,-x,sand) for y, x, sand in left]
up = [(x,y,sand) for y, x, sand in left]
down = [(-x,y,sand) for y, x, sand in left]
# 출발지
s_x = s_y = N//2

cnt = 0
move_len = 0
pos = ((0,-1), (1,0), (0, 1), (-1,0))
y, x = s_y, s_x

def sand_wind(i,j,direction):
    global result

    y, x = i, j
    total = 0
    for dy, dx, ratio in direction:
        ny = dy + y
        nx = dx + x
        if ratio == 0:  # a(나머지)
            new_sand = A[y][x] - total
        else:  # 비율
            new_sand = int(A[y][x] * ratio)
            total += new_sand

        if 0 <= nx < N and 0 <= ny < N:  # 인덱스 범위이면 값 갱신
            A[ny][nx] += new_sand
        else:  # 범위 밖이면 ans 카운트
            result += new_sand

result = 0
while True:
    if y == 0 and x == 0:
        break
    if cnt % 2 == 0:
        move_len += 1
    if cnt == 0:
        direction = left
    elif cnt == 1:
        direction = down
    elif cnt == 2:
        direction = right
    elif cnt == 3:
        direction = up

    for _ in range(move_len):
        y = y + pos[cnt][0]
        x = x + pos[cnt][1]
        sand_wind(y, x, direction)
        if y == 0 and x == 0:
            break
    cnt += 1
    cnt %= 4

print(result)


