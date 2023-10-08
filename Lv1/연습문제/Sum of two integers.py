def solution(a, b):
    x = min(a, b)
    y = max(a, b)
    answer = sum(range(x, y+1))
    return answer
