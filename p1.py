# 오픈채팅방, 220515


def solution(record):
    record_list = []
    user_list = {}
    for i in range(len(record)):
        record_list.append(record[i].split())
    for i in range(len(record)):
        if record_list[i][0] == 'Enter' or record_list[i][0] == 'Change':
            user_list[record_list[i][1]] = record_list[i][2]

    answer = []
    for i in range(len(record_list)):
        if record_list[i][0] == 'Enter':
            answer.append(user_list[record_list[i][1]] + '님이 들어왔습니다.' )
        elif record_list[i][0] == 'Leave':
            answer.append(user_list[record_list[i][1]] + '님이 나갔습니다.')

    return answer