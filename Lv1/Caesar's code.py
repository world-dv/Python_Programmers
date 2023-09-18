def solution(s, n):
    answer = ''
    for i in s:
        if i == ' ':
            answer += ' '
            continue
        elif i.islower():
            ch = 'a'
        else:
            ch = 'A'
        answer += chr(ord(ch) + (ord(i) + n - ord(ch)) % 26)
    return answer
