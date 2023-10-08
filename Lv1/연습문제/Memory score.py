def solution(name, yearning, photo):
    answer = [0] * len(photo)
    arr = {}
    
    for i, j in zip(name, yearning):
        arr[i] = j
        
    for i, j in enumerate(photo):
        answer[i] = 0
        for z in j:
            if z in arr:
                if z in arr:
                    answer[i] += arr[z]
    
    return answer
