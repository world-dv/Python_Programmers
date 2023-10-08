def solution(arr, flag):
    answer = []
    for i, j in zip(arr, flag):
        if j:
            for z in range(i * 2):
                answer.append(i)
        else:
            for z in range(i):
                answer.pop() 
    return answer
