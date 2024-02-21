from collections import defaultdict
from itertools import permutations
def solution(user_id, banned_id):
    answer = []
    
    dic = defaultdict(list)
    for i in banned_id:
        dic[i] = []
        for jidx, j in enumerate(user_id):
            if compare(i, j):
                dic[i].append(j)
    
    for p in list(permutations(user_id, len(banned_id))):
        cnt = 0
        for a, b in zip(p, banned_id):
            if a in dic[b]:
                cnt += 1
        if cnt == len(banned_id):
            if sorted(p) not in answer:
                answer.append(sorted(p))
    
    return len(answer)

def compare(banned, user):
    cnt = 0
    for i, j in zip(user, banned):
        if j == '*' or i == j:
            cnt += 1
    return cnt == len(banned) == len(user)
