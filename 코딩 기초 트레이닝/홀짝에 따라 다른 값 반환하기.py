def solution(n):
    answer = sum([i for i in range(1, n+1, 2)]) if n % 2 != 0 else sum([i * i for i in range(2, n+1, 2)])
    return answer
