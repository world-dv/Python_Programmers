def solution(intStrs, k, s, l):
    answer = []
    for i in intStrs :
        a = int(i[s:s+l]) if int(i[s:s+l]) > k else 0
        if a != 0 : answer.append(a)
    return answer
