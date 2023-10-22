def solution(s1, s2):
    answer = sum([1 if i in s2 else 0 for i in s1])
    return answer
