def solution(arr, intervals):
    answer = []
    for i in intervals:
        a, b = i
        answer.append(arr[a:b+1])
    return sum(answer, [])
