from collections import defaultdict, Counter
def solution(topping):
    answer = 0
    
    mine = Counter(topping)
    brothers = defaultdict(list)
    
    for i, j in enumerate(topping):
        if j in brothers:
            brothers[j] += 1
        else:
            brothers[j] = 1
        mine[j] -= 1
        
        if mine[j] == 0:
            del mine[j]
            
        if len(mine) == len(brothers):
            answer += 1
    
    return answer
