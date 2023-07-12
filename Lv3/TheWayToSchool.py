def solution(m, n, puddles):
    answer = 0
    
    arr = [[1 for i in range(m)] for j in range(n)]
    
    for x, y in puddles:
        arr[y-1][x-1] = 0

    for i in range(m):
        if arr[0][i] == 0:
            for j in range(i+1, m):
                arr[0][j] = 0
            break
            
    for i in range(n):
        if arr[i][0] == 0:
            for j in range(i+1, n):
                arr[j][0] = 0
            break
    
    for i in range(1, n):
        for j in range(1, m):
            if arr[i][j] != 0:
                arr[i][j] = (arr[i-1][j] + arr[i][j-1]) % 1000000007
    
    answer = arr[n-1][m-1] % 1000000007
    return answer
