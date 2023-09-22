def solution(n):
    answer = 0
    
    arr = [0, 0] + [1 for i in range(n-1)]
    for i in range(2, int(n**0.5)+1):
        if arr[i]:
            for j in range(i + i, n + 1, i):
                arr[j] = 0
            
    return arr.count(1)
