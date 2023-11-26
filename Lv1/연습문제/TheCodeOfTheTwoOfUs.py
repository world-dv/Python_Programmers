def solution(s, skip, index):
    answer = ''
    arr = 'abcdefghijklmnopqrstuvwxyz'
    for i in skip:
        arr = arr.replace(i, '')
    for i in s:
        answer += arr[(arr.index(i) + index) % len(arr)]
    return answer
