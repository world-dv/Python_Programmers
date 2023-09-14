def solution(n, words):
    answer = [0, 0]
    arr = []
    
    for i, j in enumerate(words):
        if not arr:
            arr.append(j)
        elif j in arr:
            answer[0] = i % n + 1
            answer[1] = (int)(i / n + 1)
            break
        else:
            if arr[-1][-1] != j[0]:
                answer[0] = i % n + 1
                answer[1] = (int)(i / n + 1)
                break
            else:
                arr.append(j)
        
    return answer
