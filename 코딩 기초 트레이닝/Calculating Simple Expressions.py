def solution(binomial):
    answer = binomial.split()
    if '+' in binomial :
        answer = int(answer[0]) + int(answer[2])
    elif '-' in binomial :
        answer = int(answer[0]) - int(answer[2])
    else :
        answer = int(answer[0]) * int(answer[2])
    return answer
