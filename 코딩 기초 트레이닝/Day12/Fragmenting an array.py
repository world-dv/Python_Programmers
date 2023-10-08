def solution(arr, query):
    answer = arr
    for i, j in enumerate(query) :
        if i % 2 == 0:
            answer = answer[:j+1]
        else:
            answer = answer[j:]
    return answer
