def solution(arr, n):
    answer = [i + n if j % 2 == 0 else i for j, i in enumerate(arr)] if len(arr) % 2 != 0 else [i + n if j % 2 != 0 else i for j, i in enumerate(arr)]
    return answer
