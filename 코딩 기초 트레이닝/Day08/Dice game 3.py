def solution(a, b, c, d):
    arr = [a, b, c, d]
    answer = 0
    for i in arr :
        if arr.count(i) == 4 :
            answer = 1111 * i
            break
        elif arr.count(i) == 3:
            answer = (10 * i + [z for z in arr if z != i][0]) ** 2
            break
        elif arr.count(i) == 2:
            answer = [z for z in arr if z != i]
            if answer[0] != answer[1] :
                answer = answer[0] * answer[1]
                break
            else :
                answer = (i + answer[0]) * (max(i, answer[0]) - min(i, answer[0]))
                break
        else :
            answer = min(arr)
    return answer
