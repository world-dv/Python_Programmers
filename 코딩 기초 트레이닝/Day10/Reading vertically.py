def solution(my_string, m, c):
    answer = ''
    while(True) :
        if c > len(my_string) :
            break
        answer += my_string[c - 1]
        c += m
    return answer
