def solution(str1, str2):
    answer = 0
    
    dic = dict()
    dic2 = dict()
    
    for i in range(len(str1) - 1):
        a = str1[i:i+2]
        if not a.isalpha():
            continue
        if a.lower() not in dic:
            dic[a.lower()] = 1
        else:
            dic[a.lower()] = dic[a.lower()] + 1
    
    for i in range(len(str2) - 1):
        a = str2[i:i+2]
        if not a.isalpha():
            continue
        if a.lower() not in dic2:
            dic2[a.lower()] = 1
        else:
            dic2[a.lower()] = dic2[a.lower()] + 1
    
    count_max = 0 #합집합
    count_min = 0 #교집합
    for i in dic:
        if i in dic2:
            count_max += max(dic[i], dic2[i])
            count_min += min(dic[i], dic2[i])
            dic2.pop(i)
        else:
            count_max += dic[i]
    for i in dic2:
        count_max += dic2[i]
    if count_max == 0:
        return 65536
    answer = int(count_min / count_max * 65536)
    return answer
