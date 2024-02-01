def solution(routes):
    answer = 0
    arr = []
    routes = sorted(routes, key = lambda x : x[1])
    
    for i, j in routes:
        if not arr:
            arr.append(j)
            continue
        if i <= arr[-1] and arr[-1] <= j:
            continue
        else:
            arr.append(j)
    answer = len(arr)
    return answer
