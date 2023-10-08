def solution(k, tangerine):
    arr = {}
    for i in tangerine:
        arr[i] = 0
    
    for i in tangerine:
        arr[i] += 1
        
    arr = sorted(arr.items(), key=lambda x:x[1], reverse=True)
    
    for i, j in enumerate(arr):
        k -= j[1]
        if k <= 0:
            return i + 1
