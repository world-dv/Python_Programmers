def solution(genres, plays):
    answer = []
    
    dic = dict()
    dic2 = dict()
    for i in list(set(genres)):
        dic[i] = []
    
    for i, j in enumerate(genres):
        dic[j].append([plays[i], i])
        if j not in dic2:
            dic2[j] = plays[i]
        else:
            dic2[j] = dic2[j] + plays[i]
    
    for i in dic:
        dic[i] = sorted(dic[i], key = lambda x : (-x[0], x[1]))
    
    dic2 = sorted(dic2.items(), key = lambda x : -x[1])
    
    for i in dic2:
        if len(dic[i[0]]) == 1:
            answer.append(dic[i[0]][0][1])
            continue
        answer.append(dic[i[0]][0][1])
        answer.append(dic[i[0]][1][1])
    
    return answer
