def solution(n):
    answer = 0
    
    arr = [0 for _ in range(n+1)]
    arr[0] = 1
    arr[2] = 3
    for i in range(4, n+1, 2):
        arr[i] = (4 * arr[i-2] - arr[i-4]) % 1000000007
    answer = arr[n]
    
    return answer
