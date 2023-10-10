def solution(n):
    answer = 0
    number = 1
    for i in range(1, n) :
        number *= i
        if number <= n :
            answer = i
        else :
            break
    
    return answer if n > 2 else n
