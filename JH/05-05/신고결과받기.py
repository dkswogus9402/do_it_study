def solution(id_list, report, k):
    answer = []  # 정답
    id_dict = {}  # id를 key값으로 한 딕셔너리
    cnt_table = {}  # 횟수를 새기 위한 딕셔너리
    stop_table = {}  # 1이면 정지 0이면 정지 X
    for id_ in id_list:
        id_dict[id_] = set()
        cnt_table[id_] = 0
        stop_table[id_] = 0

    for value in report:
        A, B = value.split(' ')
        id_dict[A].add(B)  # 신고한 ID

    for key, value in id_dict.items():
        for v in value:
            cnt_table[v] += 1
    # 검사
    for key, value in cnt_table.items():
        if value >= k:
            stop_table[key] = 1

    answer = []
    # 정지된 것과 비교
    for key, value in id_dict.items():
        cnt = 0
        for v in value:
            if stop_table[v] == 1:
                cnt += 1
        answer.append(cnt)
    return answer