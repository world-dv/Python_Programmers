def solution(arr, queries):
    answer = arr
    for i in queries:
        a, b = i
        for z in range(a, b+1):
            answer[z] += 1
    return answer
