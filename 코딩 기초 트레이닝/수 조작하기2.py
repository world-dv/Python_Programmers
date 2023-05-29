def solution(numLog):
    answer = ''
    log = { 1 : "w", -1 : "s", 10 : "d", -10 : "a"}
    for i in range(len(numLog) - 1) :
        answer += log[numLog[i + 1] - numLog[i]]
    return answer
