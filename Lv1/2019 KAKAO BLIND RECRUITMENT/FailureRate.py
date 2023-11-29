def solution(N, stages):
    dic = dict()
    for i in range(1, N+1):
        c = len([j for j in stages if j >= i])
        if c == 0:
            dic[i] = 0
            continue
        dic[i] = stages.count(i) / c
    answer = sorted(dic, key=lambda x : -dic[x])
    return answer
