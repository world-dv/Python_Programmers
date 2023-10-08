def solution(k, m, score):
    answer = 0
    count = 0
    arr = []
    score = sorted(score, reverse=True)
    for i in score:
        arr.append(i)
        count += 1
        if count == m:
            x = min(arr)
            if 1 <= x and x <= k:
                answer += min(arr) * m
            count = 0
            arr.clear()
    
    return answer
