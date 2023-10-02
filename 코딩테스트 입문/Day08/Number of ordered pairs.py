def solution(n):
    n1 = int(n ** (1/2)) #제곱근
    answer = 0
    
    for i in range(1, n1+1) :
        if n % i == 0 :
            answer += 1 if n // i == i else 2
    
    return answer
