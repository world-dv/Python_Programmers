def solution(s):
    answer = []
    arr = dict()
    for i, j in enumerate(s):
        if j not in arr:
            answer.append(-1)
        else:
            answer.append(i - arr[j])
        arr[j] = i
    return answer
