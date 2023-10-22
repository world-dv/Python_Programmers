def solution(num, k):
    num = str(num)
    answer = num.index(str(k)) + 1 if str(k) in num else -1
    return answer
