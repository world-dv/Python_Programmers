def solution(cards):
    answer = []
    visited = [0 for _ in range(len(cards))]
    for i in range(len(cards)):
        #카운트 -> 결과 반환
        answer.append(countResult(cards, visited, i-1))
    answer = sorted(answer)
    if len(answer) > 1:
        return answer[-1] * answer[-2]
    return 0

def countResult(cards, visited, i):
    result = 0
    card = cards[i] - 1
    while True:
        if not visited[card]:
            visited[card] = 1
            result += 1
            card = cards[card] - 1
        else:
            break

    return result
