def solution(a, b):
    a1 = int(str(a) + str(b))
    a2 = 2 * a * b
    return a1 if a1 > a2 else a2
