def solution(left, right):
    answer = 0
    for i in range(left, right+1):
        if countNumber(i) % 2 == 0:
            answer += i
        else:
            answer -= i
    return answer

def countNumber(x):
    c = 0
    for i in range(1, x+1):
        if x % i == 0:
            c += 1
    return c
