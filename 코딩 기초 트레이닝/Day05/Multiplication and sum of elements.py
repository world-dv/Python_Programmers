def solution(num_list):
    answer = 1
    for i in num_list :
        answer *= i
    return int(answer < sum(num_list) ** 2)
