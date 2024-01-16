import math
def solution(n,a,b):
    answer = 0
    count = 0
    while count < n:
        a = math.ceil(a / 2)
        b = math.ceil(b / 2)
        count += 1
        if a == b:
            break
    return count
