def solution(s):
    answer = ''
    for i in range(len(s)):
        if s[i].isalpha():
            if i == 0 or s[i-1] == ' ':
                answer += s[i].upper()
            else: 
                answer += s[i].lower()
        else:
            answer += s[i]
                
    return answer
