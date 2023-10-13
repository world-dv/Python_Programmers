def solution(array, n):
    answer = min([n - i if n - i > 0 else -1 * (n - i) for i in array])
    answer = n - answer if n - answer in array else n + answer
    return answer
