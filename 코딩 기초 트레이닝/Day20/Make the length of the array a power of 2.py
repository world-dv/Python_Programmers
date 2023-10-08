def solution(arr):
    a = 0
    b = 0
    while a < len(arr):
        a = 2 ** b
        b += 1
    answer = [arr[i] if len(arr) > i else 0 for i in range(a)]
    return answer 
