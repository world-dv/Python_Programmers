def solution(str_list):
    answer = []
    a = -1
    b = -1
    if 'l' in str_list:
        a = str_list.index('l')
    if 'r' in str_list:
        b = str_list.index('r')  
    if a == b and a == -1: 
        return []
    if a == -1 and b != -1:
        return str_list[b+1:]
    if a != -1 and b == -1:
        return str_list[:a]
    if a != -1 and b != -1:
        return str_list[:a] if a < b else str_list[b+1:]
    return answer
