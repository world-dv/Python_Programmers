from collections import defaultdict
def solution(gems):
    answer = []
    g = list(set(gems))
    min_len = len(gems) + 1
    dic = defaultdict(int)
    end = 0
    for i in range(len(gems)):
        while len(dic) < len(g) and end < len(gems):
            dic[gems[end]] += 1
            end += 1
        if min_len > end - i and len(dic) == len(g):
            min_len = end - i
            answer = [i + 1, end]
        dic[gems[i]] -= 1
        if dic[gems[i]] == 0:
            del dic[gems[i]]
    return answer
