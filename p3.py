# 추석 트래픽 계산

def solution(lines):
    time = []
    for i in range(len(lines)):
        tmp = lines[i].split()
        tmp_time = tmp[1].split(':')
        tmp_time = float(tmp_time[0])*3600+float(tmp_time[1])*60+float(tmp_time[2])
        time.append([tmp_time - (float(tmp[2].strip('s')) - 0.001), tmp_time])
    def isinthebar(start_time, end_time, second):
        if second <= start_time <= round(second + 0.999, 3) or second <= end_time <= round(second + 0.999, 3):
            return True
        elif start_time < second and end_time > round(second + 0.999, 3):
            return True
        else:
            return False
    answer = [0] * len(lines)
    for i in range(len((lines))):
        for j in range(len(time)):
            if isinthebar(time[j][0], time[j][1], time[i][1]):
                answer[i] += 1
    return max(answer)

# test case
# print(solution(
# ["2016-09-15 20:59:57.421 0.351s", "2016-09-15 20:59:58.233 1.181s", "2016-09-15 20:59:58.299 0.8s",
# "2016-09-15 20:59:58.688 1.041s", "2016-09-15 20:59:59.591 1.412s", "2016-09-15 21:00:00.464 1.466s",
# "2016-09-15 21:00:00.741 1.581s", "2016-09-15 21:00:00.748 2.31s", "2016-09-15 21:00:00.966 0.381s",
# "2016-09-15 21:00:02.066 2.62s"]))
