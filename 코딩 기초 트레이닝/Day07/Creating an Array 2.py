def solution(l, r):
    answer = []
    for i in range(l, r + 1) :
        a = 1
        for j in str(i) :
            if int(j) % 5 != 0:
                a = 0
                break
        if a != 0 :
            answer.append(i)
    if not answer :
        answer.append(-1)
    return answer
