
'''
냄새 코딩 방법
N 값만 보고, BFS DFS 구분하기

1 ~ 30 : DFS
2차원 배열이 나오면서 N값이 50~200수준 최소를 구해라 : BFS
가능성이 크다

이해를 꼼꼼히 해야하고
N 확인

예제 검증 -> 손으로 왜 입력데이터가 출력데이터가 되는지 확인
-> 손으로 검증한 것을 기반으로 디버깅을 한다.

문제 이해 -> 설계단계 -> 계획 세우기
'''

def BFS():
    for i in range(5):
        for j in range(5):
            if A[i][j] == 1:
                s_y, s_x = i, j
    queue = []
    visited = [[0] * 5 for _ in range(5)]

    visited[s_y][s_x] = 1
    queue.append([s_y, s_x])

    pos = [[1,0], [-1,0], [0, 1], [0, -1]]
    while queue:
        y, x = queue.pop(0)
        for dy, dx in pos:
            ny = dy + y
            nx = dx + x
            if 0 <= ny < 5 and 0 <= nx < 5 and visited[ny][nx] == 0:
                queue.append([ny, nx])
                visited[ny][nx] = visited[y][x] + 1

    for a in visited:
        print(a)

A = [[0,0,0,0,0],
    [0,1,0,0,0],
    [0,0,0,0,0],
    [0,0,0,0,0],
    [0,0,0,0,0]]

BFS()