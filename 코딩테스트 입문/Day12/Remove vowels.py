def solution(my_string):
    answer = ''.join([i for i in my_string if i not in 'aeiou'])
    return answer
