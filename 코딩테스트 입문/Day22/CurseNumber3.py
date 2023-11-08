def solution(n):
    answer = 1
    count = 1
    
    while(True):
        if answer % 3 == 0 or '3' in str(answer):
            answer += 1
            continue
        if count == n:
            break
        count += 1
        answer += 1
    
    return answer
