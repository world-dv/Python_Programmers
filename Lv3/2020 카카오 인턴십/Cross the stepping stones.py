import heapq
def solution(stones, k):
    st = [[-1 * j, i] for i, j in enumerate(stones[:k])]
    heapq.heapify(st)
    answer = [st[0][0]]
    for i in range(k, len(stones)):
        heapq.heappush(st, [-stones[i], i])
        while st[0][1] <= i - k: 
            heapq.heappop(st)
        answer.append(st[0][0])
    return -1 * max(answer)
