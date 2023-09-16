def solution(prices):
    answer = []
    l = len(prices) - 1
    for i, j in enumerate(prices) :
        if i == l:
            answer.append(0)
            break
        else:
            sec = 1
            idx = i + 1
            while(idx < l and j <= prices[idx]):
                idx += 1
                sec += 1
            answer.append(sec)
    return answer
