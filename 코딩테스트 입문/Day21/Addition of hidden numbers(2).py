def solution(my_string):
    answer = 0
    a = ''
    for i in my_string:
        if i.isdigit():
            a += i
        if i.isalpha():
            answer += int(a) if a != '' else 0
            a = ''
    return answer + int(a) if a != '' else answer
