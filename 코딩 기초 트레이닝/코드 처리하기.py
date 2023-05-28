def solution(code):
    answer = ''
    mode = 0
    for i in range(0, len(code)) :
        if code[i] == "1" :
            mode = not(mode)
            continue
        
        if mode == 1 and i % 2 != 0:
            answer += code[i]
        elif mode == 0 and i % 2 == 0 :
            answer += code[i]
    
    if len(answer) == 0 :
        answer = "EMPTY"
    return answer
