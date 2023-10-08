def solution(food):
    answer = ''
    arr = []
    for i, j in enumerate(food):
        answer += str(i) * (j // 2)

    answer = answer + '0' + answer[::-1]
    return answer
