def solution(id_list, report, k):
    answer = []
    dic = dict()
    dic3 = dict()
    for i in id_list:
        dic[i] = []
        dic3[i] = []
        
    for i in report:
        a = i.split(' ')
        if a[0] not in dic[a[1]]:
            dic[a[1]].append(a[0])
        if a[1] not in dic3[a[0]]:
            dic3[a[0]].append(a[1])
        
    for i in id_list:
        answer.append(0)
        for j in dic3[i]:
            if len(dic[j]) >= k:
                answer[-1] += 1
    return answer
