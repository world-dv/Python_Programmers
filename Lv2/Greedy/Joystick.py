def solution(name):
    answer = 0
    
    move = len(name) - 1
    for j, i in enumerate(name):
        answer += min(ord(i) - ord('A'), ord('Z') - ord(i) + 1)
        
        next_idx = j + 1
        while next_idx < len(name) and name[next_idx] == 'A':
            next_idx += 1
        move = min(move, 2 * j + len(name) - next_idx, (2 * (len(name) - next_idx)) + j)
    
    return answer + move
