def solution(board, moves):
    answer = 0
    arr = []
    for i in moves:
        for h, j in enumerate(board):
            if j[i-1] != 0:
                if not arr:
                    arr.append(j[i-1])
                    board[h][i-1] = 0
                    break
                if j[i-1] == arr[-1]:
                    arr.pop()
                    answer += 1
                else:
                    arr.append(j[i-1])
                board[h][i-1] = 0
                break     
    return answer * 2
