def solution(n):
    answer = int(n ** (1/2)) ** 2 == n
    return 1 if answer else 2
