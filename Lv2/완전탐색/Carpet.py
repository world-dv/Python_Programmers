def solution(brown, yellow):
    answer = []
    for col in range(1, yellow + 1):
        if yellow % col == 0:
            row = yellow // col
            if row * 2 + col * 2 + 4 == brown:
                answer.append(row + 2)
                answer.append(col + 2)
                break
    return answer
