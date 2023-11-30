def solution(participant, completion):
    answer = ''
    h = 0
    dic = dict()
    for i in participant:
        dic[int(hash(i))] = i
        h += int(hash(i))
    for j in completion:
        h -= int(hash(j))
    answer = dic[h]
    return answer
