def solution(t, p):
    answer = 0
    a = len(p)
    answer = sum([int(t[i:i+a]) <= int(p) for i in range(len(t) - a + 1)])
    return answer
