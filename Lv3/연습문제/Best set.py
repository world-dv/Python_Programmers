def solution(n, s):
    answer = []
    N = n
    for i in range(N):
        start = s // n
        if start == 0:
            answer = [-1]
            break
        answer.append(start)
        s -= start
        n -= 1
    return answer
