import math
def solution(k, d):
    answer = 0
    
    for y in range(0, d+1, k):
        x = int(math.sqrt(d ** 2 - y ** 2))
        answer += x // k + 1
    
    return answer
