def solution(n, lost, reserve):
    answer = 0
    visited = [1 for i in range(n)]
    lost.sort()
    reserve.sort()
    
    for i in lost:
        if i in reserve:
            visited[i-1] = 1
            reserve.pop(reserve.index(i))
        else:
            visited[i-1] = 0
    
    for j in reserve:
        value = j - 1
        if value == 0:
            if not visited[value + 1]:    
                visited[value + 1] = 1
        elif value == n - 1:
            if not visited[value - 1]:
                visited[value - 1] = 1
        else:
            if not visited[value - 1]:
                visited[value - 1] = 1
            elif not visited[value + 1]:    
                visited[value + 1] = 1
    answer = len([i for i in visited if i != 0])
    return answer
