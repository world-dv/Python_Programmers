def solution(n, lost, reserve):
    answer = 0
    
    arr = [i for i in lost if i not in reserve]
    arr2 = [i for i in reserve if i not in lost]
    arr.sort()
    arr2.sort()
    
    for i in arr2:
        if i-1 in arr:
            arr.remove(i-1)
        elif i+1 in arr:
            arr.remove(i+1)
    
    answer = n - len(arr)
    
    return answer
