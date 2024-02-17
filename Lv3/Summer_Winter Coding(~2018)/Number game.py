def solution(A, B):
    answer = 0
    A = sorted(A)
    B = sorted(B)
    for i in A:
        for jdx in range(len(B)):
            if B[jdx] > i:
                B.pop(jdx)
                answer += 1
                break
    return answer
