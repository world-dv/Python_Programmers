def solution(my_string, num1, num2):
    answer = list(my_string)
    answer[num2], answer[num1] = my_string[num1], my_string[num2] 
    return ''.join(answer)
