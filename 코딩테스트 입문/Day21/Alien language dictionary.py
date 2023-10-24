def solution(spell, dic):
    answer = 2
    for i in dic:
        a = ''
        for j in spell:
            a += str(i.count(j))
        if a.count('1') == len(spell):
            return 1
    return answer
