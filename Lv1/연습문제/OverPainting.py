def solution(n, m, section):
    answer = 0
    mark = 0
    if m == 1:
        return len(section)
    for idx in section:
        if idx >= mark:
            mark = idx + m
            answer += 1
    return answer
