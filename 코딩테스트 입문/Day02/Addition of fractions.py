def solution(numer1, denom1, numer2, denom2):
    answer = []
    
    a = denom2 * numer1 + denom1 * numer2
    b = denom1 * denom2
    
    for i in range(b, 1, -1):
        if a % i == 0 and b % i == 0:
            a = a // i
            b = b // i
            break
    
    answer.append(a)
    answer.append(b)
    
    return answer
