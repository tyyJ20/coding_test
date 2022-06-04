# 문자열 압축
# 테스트 통과 못함


def datacompress(s, n):
    divide_time = int(len(s) // n)
    divide_n_list = []
    for i in range(divide_time):
        slice_s = s[(i * n):((i + 1) * n)]
        divide_n_list.append(slice_s)

    compression_time = [0]
    k = 0
    while len(divide_n_list) > 1:
        if divide_n_list[0] == divide_n_list[1]:
            compression_time[k] += 1
            del divide_n_list[0]
        else:
            if not compression_time[k] == 0:
                compression_time.append(0)
                k += 1
            del divide_n_list[0]
    if compression_time[-1] == 0:
        compression_time.remove(0)

    answer = len(s) - n * sum(compression_time) + len(compression_time)
    return answer

def solution(s):
    if len(s) == 1:
        return 1

    repeat_time = int(len(s) // 2)

    compressed_value_list = []
    for i in range(1, repeat_time + 1):
        compressed_value_list.append(datacompress(s, i))

    return min(compressed_value_list)