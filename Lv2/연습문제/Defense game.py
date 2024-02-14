import heapq
def solution(n, k, enemy):
    answer = 0
    total = 0
    heap = []
    for i in enemy:
        heapq.heappush(heap, -i)
        total += i
        if total > n:
            if k == 0:
                break
            total += heapq.heappop(heap)
            k -= 1
        answer += 1
    
    return answer
