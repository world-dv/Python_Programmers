def solution(num_list):
    answer = [0] * 2
    for i in num_list:
        answer[i % 2] += 1
    return answer
