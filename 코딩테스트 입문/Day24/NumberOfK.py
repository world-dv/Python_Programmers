def solution(i, j, k):
    answer = 0
    for idx in range(i, j+1):
        if str(k) in str(idx):
            answer += str(idx).count(str(k))
    return answer
