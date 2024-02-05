import math
def solution(arrayA, arrayB):
    answer = 0
        
    a = arrayA[0]
    b = arrayB[0]
    for i in range(1, len(arrayA)):
        a = math.gcd(a, arrayA[i])
        b = math.gcd(b, arrayB[i])
    
    cnt_a = 0
    cnt_b = 0
    for i, j in zip(arrayA, arrayB):
        if a != 1 and j % a != 0:
            cnt_a += 1
        if b != 1 and i % b != 0:
            cnt_b += 1
    if cnt_a == len(arrayA) or cnt_b == len(arrayB):
        answer = max(a, b)
    else:
        answer = 0
    
    return answer
