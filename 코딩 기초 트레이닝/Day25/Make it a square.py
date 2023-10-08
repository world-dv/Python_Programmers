def solution(arr):
    l = max(len(arr), len(arr[0]))
    answer = [[0 for i in range(l)] for j in range(l)]
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            answer[i][j] = arr[i][j]
    return answer
