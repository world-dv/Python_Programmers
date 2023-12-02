def solution(d, budget):
    answer = []
    d = sorted(d)
    for i in d:
        answer.append(i)
        if sum(answer) > budget:
            answer.pop()
    return len(answer)
