def solution(s):
    answer = ''
    count = 0
    for i in s:
        if i == ' ':
            answer += i
            count = 0
            continue
        elif count % 2 == 0:
            answer += i.upper()
        else:
            answer += i.lower()
        count += 1
    
    return answer
