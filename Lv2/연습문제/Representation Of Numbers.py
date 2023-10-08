def solution(n):
    answer = 0
    idx = 1
    while idx <= n:
        s = 0
        for i in range(idx, n+1):
            s += i
            if s == n:
                answer += 1
                break
            elif s > n:
                break
        idx += 1
            
    return answer
