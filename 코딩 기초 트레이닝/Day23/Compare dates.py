def solution(date1, date2):
    answer = 0
    for i, j in zip(date1, date2):
        if i < j:
            answer = 1
            break
        elif i > j:
            answer = 0
            break
    return answer
