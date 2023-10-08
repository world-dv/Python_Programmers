def solution(rank, attendance):
    answer = 0
    arr = []
    for i, j in zip(rank, attendance):
        if j:
            arr.append(i)
    arr = sorted(arr)[:3]
    answer = 10000 * rank.index(arr[0]) + 100 * rank.index(arr[1]) + rank.index(arr[2])
    return answer
