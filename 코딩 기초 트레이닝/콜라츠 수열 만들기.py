def solution(n):
    answer = []
    while True:
        answer.append(n)
        if n == 1 :
            break
        n = n / 2 if n % 2 == 0 else 3 * n + 1
    return answer
