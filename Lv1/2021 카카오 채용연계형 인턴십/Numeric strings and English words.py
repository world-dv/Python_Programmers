def solution(s):
    answer = s
    arr = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    for j, i in enumerate(arr):
        answer = answer.replace(i, str(j))
    return int(answer)
