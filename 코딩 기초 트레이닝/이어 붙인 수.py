def solution(num_list):
    answer = int("".join(str(i) for i in num_list if i % 2 == 0)) + int("".join(str(j) for j in num_list if j % 2 != 0))
    return answer
