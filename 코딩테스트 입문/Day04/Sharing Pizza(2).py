def solution(n):
    answer = 0
    i = 1
    while True:
        if (i * n) % 6 == 0:
            answer = i * n // 6
            break
        i += 1
    return answer
