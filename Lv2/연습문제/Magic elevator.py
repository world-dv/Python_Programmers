def solution(storey):
    answer = 0
    
    while storey > 0:
        a = storey % 10
        if a > 5:
            storey += 10
            answer += 10 - a
        elif a < 5:
            answer += a
        else:
            if (storey // 10) % 10 >= 5:
                storey += 10
            answer += a
        storey //= 10
    
    return answer
