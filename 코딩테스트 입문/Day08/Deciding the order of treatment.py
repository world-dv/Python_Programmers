def solution(emergency):
    answer = [0] * len(emergency)
    arr = sorted(emergency, reverse=True)
    for i, j in enumerate(emergency):
        answer[i] = arr.index(j) + 1
    return answer
