import heapq
def solution(operations):
    arr = []
    
    for i in operations:
        a = i.split(' ')
        if a[0] == 'I':
            heapq.heappush(arr, int(a[1]))
        elif a[0] == 'D':
            if arr == []:
                continue
            if a[1] == '-1':
                heapq.heappop(arr)
            else:
                arr.pop()
    if arr == []:
        return [0, 0]
    
    return [max(arr), min(arr)]
