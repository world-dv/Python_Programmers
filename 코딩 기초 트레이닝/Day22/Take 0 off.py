def solution(n_str):
    answer = ''
    for j, i in enumerate(n_str) :
        if i != '0' :
            answer = n_str[j:]
            break
    return answer
