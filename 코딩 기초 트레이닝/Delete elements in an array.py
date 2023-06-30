def solution(arr, delete_list):
    answer = []
    for i in arr :
        answer.append(i)
        for j in delete_list :
            if i == j :
                answer.pop()
                break
    return answer
