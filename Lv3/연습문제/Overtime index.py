import heapq

def solution(n, works):
    answer = 0
    
    heap = []
    for i in works:
        heapq.heappush(heap, -i)
    
    while n != 0:
        if len(heap) > 0:
            a = heapq.heappop(heap)
            n -= 1
            if a == -1:
                continue
            heapq.heappush(heap, a + 1)
        else:
            break
    
    for i in heap:
        answer += abs(i) ** 2
    
    return answer
