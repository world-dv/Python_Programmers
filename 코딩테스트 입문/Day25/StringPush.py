def solution(A, B):
    answer = 0
    
    while(True):
        if A == B:
            break
        if answer == len(A):
            answer = -1
            break
        answer += 1
        A = A[-1] + A[:-1]
    
    return answer
