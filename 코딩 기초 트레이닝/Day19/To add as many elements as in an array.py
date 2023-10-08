def solution(arr):
    answer = [[i] * i for i in arr]
    return sum(answer, [])
