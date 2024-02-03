def solution(sequence, k):
    answer = []
    
    start, end = 0, 0
    min_len = len(sequence) + 1
    
    total = sequence[start]
    
    while start <= end < len(sequence):
        if total == k:
            if end - start + 1 < min_len:
                min_len = end - start + 1
                answer = [start, end]
            total -= sequence[start]
            start += 1
        elif total < k:
            end += 1
            if end < len(sequence):
                total += sequence[end]
        elif total > k:
            total -= sequence[start]
            start += 1
    return answer
