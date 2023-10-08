def solution(a, b):
    a1 = int(str(a) + str(b))
    a2 = int(str(b) + str(a))
    return a1 if a1 > a2 else a2
