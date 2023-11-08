def solution(score):
    answer = []
    
    arr = sorted([sum(i) for i in score], reverse=True)
    d = dict()
    prize = 1
    for i in arr:
        if i not in d:
            d[i] = prize
            if arr.count(i) > 1:
                prize += arr.count(i)
            else:
                prize += 1
    answer = [d[sum(i)] for i in score]
    return answer
