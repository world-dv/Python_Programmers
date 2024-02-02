def solution(order):
    answer = 0
    arr = []
    end = 0
    for i, j in enumerate(order):
        if not arr or j >= end:
            arr += [i for i in range(end, j)]
            end = j+1
            answer += 1
        elif arr[-1] == j:
            arr.pop()
            answer += 1
        else:
            break
    
    return answer
