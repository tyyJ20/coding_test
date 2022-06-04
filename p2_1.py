# 문자열 압축


def solution(s):
    if len(s) == 1:
        return 1
    result = []
    for i in range(1, len(s) // 2 + 1):
        tmp = ''
        coefficient = 1
        for j in range(0, len(s) // i):
            if s[i*j : i*j + i] == s[i*j + i : i*j + 2*i]:
                coefficient += 1
            else:
                if coefficient > 1:
                    tmp += str(coefficient) + s[i*j : i*j + i]
                    coefficient = 1
                else:
                    tmp += s[i*j : i*j + i]
        if len(s)%i != 0:
            tmp += s[-(len(s)%i):]
        result.append(len(tmp))
    return min(result)