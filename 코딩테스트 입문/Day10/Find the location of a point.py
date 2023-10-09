def solution(dot):
    answer = 0
    if dot[0] < 0 :
        answer = 2 if dot[1] > 0 else 3
    else :
        answer = 1 if dot[1] > 0 else 4
    return answer
