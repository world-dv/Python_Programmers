def solution(array):
    answer = 0
    arr = set(array)
    a = -1
    for i in arr:
        if a < array.count(i):
            a = array.count(i)
            answer = i
        elif a == array.count(i):
            answer = -1
    return answer
