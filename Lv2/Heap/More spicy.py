import heapq

def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    
    while True:
        a = heapq.heappop(scoville)
        if a < K:
            if len(scoville) == 0:
                return -1 
            heapq.heappush(scoville, a + heapq.heappop(scoville) * 2)
            answer += 1
        else:
            break
    
    return answer 
