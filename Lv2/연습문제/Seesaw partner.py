from collections import defaultdict
def solution(weights):
    answer = 0
    dic = defaultdict(int)
    
    for i in weights:
        answer += dic[i]
        answer += dic[(i * 2) / 3] + dic[(i * 3) / 2]
        answer += dic[(i * 2) / 4] + dic[(i * 4) / 2]
        answer += dic[(i * 3) / 4] + dic[(i * 4) / 3]
        dic[i] += 1
    return answer
