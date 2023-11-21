def solution(clothes):
    answer = 1
    dic = dict()
    for i, j in clothes:
        dic[j] = sum([1 if j == b else 0 for a, b in clothes])
    for i in dic:
        answer *= dic[i] + 1
    return answer - 1
