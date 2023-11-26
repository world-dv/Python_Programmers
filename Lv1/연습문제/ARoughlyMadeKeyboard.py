def solution(keymap, targets):
    answer = []
    dic = dict()
    for i in keymap:
        for j in i:
            if j in dic:
                dic[j] = min(dic[j], i.index(j) + 1)
                continue
            dic[j] = i.index(j) + 1
    for i in targets:
        a = 0
        for j in i:
            if j not in dic:
                a = -1
                break
            a += dic[j]
        answer.append(a)
    return answer
