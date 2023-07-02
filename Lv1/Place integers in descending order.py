def solution(n):
    answer = int(''.join(sorted(list(str(n)))[::-1]))
    return answer
