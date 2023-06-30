def solution(numbers, n):
    answer = sum([j for i, j in enumerate(numbers) if n >= sum(numbers[:i])])
    return answer
