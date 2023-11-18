def solution(n):
    fibo = [i for i in range(n+1)]
    for i in range(2, len(fibo)):
        fibo[i] = fibo[i-2] + fibo[i-1] 
    
    answer = fibo[n] % 1234567
    return answer
