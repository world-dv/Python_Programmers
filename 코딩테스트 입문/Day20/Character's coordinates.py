def solution(keyinput, board):
    answer = [0, 0]
    for i in keyinput :
        if i == "left" :
            answer[0] -= 1 
        if i == "right" :
            answer[0] += 1 
        if i == "up" :
            answer[1] += 1 
        if i == "down" :
            answer[1] -= 1
        if abs(answer[0]) > board[0] // 2 :
            answer[0] += 1 if i == "left" else -1
        if abs(answer[1]) > board[1] // 2 :
            answer[1] += 1 if i == "down" else -1
    return answer
