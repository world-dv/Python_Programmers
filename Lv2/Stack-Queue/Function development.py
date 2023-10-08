def solution(progresses, speeds):
    answer = []
    arr = []
    m = 0
    for i, j in zip(progresses, speeds):
        k = (100 - i) // j + (1 if (100 - i) % j != 0 else 0)
        if m < k:
            m = k
            answer.append(1)
        else:
            answer[-1] += 1
    return answer
