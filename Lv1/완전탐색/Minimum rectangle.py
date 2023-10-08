def solution(sizes):
    answer = 0
    
    a = list(map(max, sizes))
    b = list(map(min, sizes))
    answer = max(a) * max(b)
    return answer
