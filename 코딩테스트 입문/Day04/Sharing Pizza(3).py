def solution(slice, n):
    answer = 1 if n % slice != 0 else 0
    return answer + n // slice
