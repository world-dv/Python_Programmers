from functools import reduce
def solution(num_list):
    answer = 0
    if len(num_list) <= 10 :
        answer = reduce(lambda x, y : x * y, num_list)
    else :
        answer = sum(num_list)
    return answer
