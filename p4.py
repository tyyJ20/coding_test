# 사칙연산, 220603
# 테스트 통과 못함


def ConvertOperator(operator):
    if operator == '+':
        return '-'
    elif operator == '-':
        return '+'


def solution(arr):
    numbers = []
    operators = []
    for i in range(0, len(arr) - 1, 2):
        numbers.append(arr[i])
        operators.append(arr[i + 1])
    numbers.append(arr[-1])

    minus_indices = []
    for i in range(len(operators) - 1):
        if operators[i] == '-':
            minus_indices.append(i)
    minus_indices.reverse()

    def DivideCase(list, indices, index=0):
        range_list = list[:]
        for case in range_list:
            tmp = case[indices[index] + 1:]
            for i in range(len(tmp)):
                tmp[i] = ConvertOperator(tmp[i])
                list.append(case[:indices[index] + 1] + tmp)
        if indices[index] == list[0].index('-'):
            return list
        return DivideCase(list, indices, index + 1)

    operators = [operators]
    operators = DivideCase(operators, minus_indices)

    result = []
    for i in operators:
        if i not in result:
            result.append(i)

    answer_list = []
    for i in range(len(result)):
        answer = int(arr[0][0])
        for j in range(len(result[i])):
            if result[i][j] == '+':
                answer += int(numbers[j + 1])
            else:
                answer -= int(numbers[j + 1])
        answer_list.append(answer)

    return max(answer_list)


# test case
# print(solution(["5", "-", "3", "+", "1", "+", "2", "-", "4"]))