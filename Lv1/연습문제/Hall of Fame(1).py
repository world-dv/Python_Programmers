def solution(k, score):
    answer = []
    arr = []
    for i in score:
        arr.append(i)
        arr = sorted(arr, reverse = True)
        if len(arr) > k:
            del arr[-1]
        answer.append(arr[-1])
    return answer
