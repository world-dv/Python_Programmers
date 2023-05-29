def solution(arr, queries):
    answer = []
    for i, j, z in queries :
        idx = []
        for x in range(i, j + 1) :
            if arr[x] > z :
                idx.append(arr[x])
        answer.append(-1) if len(idx) == 0 else answer.append(min(idx))
    return answer
