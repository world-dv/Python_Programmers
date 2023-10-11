def solution(n):
    answer = []
    arr = []
    
    a = 2
    i = 2
    while a * i <= n :
        arr.append(a * i)
        i += 1
        if i == 10 :
            i = 2
            a += 1
    a = 2
    while a <= n :
        if a not in arr and n % a == 0:
            answer.append(a)
            n //= a
        a += 1
    
    return answer
