def solution(triangle):
    answer = 0
    n = len(triangle)
    
    arr = [[0 for i in range(len(triangle[-1]))] for j in range(n)]
    arr[0][0] = triangle[0][0]
    
    for i in range(n - 1):
        for j in range(len(triangle[i])):
            arr[i+1][j] = max(arr[i+1][j], arr[i][j] + triangle[i+1][j])
            arr[i+1][j+1] = max(arr[i+1][j+1], arr[i][j] + triangle[i+1][j+1])
    
    answer = max(arr[-1])
    return answer
