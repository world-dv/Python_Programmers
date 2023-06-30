def solution(num_list):
    a = sum([i for j,i in enumerate(num_list) if j % 2 == 0]) 
    b = sum([i for j,i in enumerate(num_list) if j % 2 != 0])
    answer = a if a >= b else b
    return answer
