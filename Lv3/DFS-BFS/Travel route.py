from collections import defaultdict
def solution(tickets):
    answer = []
    
    dic = defaultdict(list)
    for i, j in tickets:
        dic[i].append(j)
    
    for i in dic:
        dic[i] = sorted(dic[i])
    
    dfs(dic, ['ICN'], answer)
    
    return answer[::-1]

def dfs(dic, path, answer):
    while path:
        start = path[-1]
        if len(dic[start]) > 0:
            path.append(dic[start].pop(0))
        else:
            answer.append(path.pop())
