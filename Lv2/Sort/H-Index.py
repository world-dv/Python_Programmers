def solution(citations):
    answer = 0
    citations = sorted(citations, reverse=True)
    for i in range(len(citations)):
        if answer < citations[i]:
            answer += 1
    return answer
