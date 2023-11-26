def solution(X, Y):
    answer = ''
    x = list(set(X))
    y = list(set(Y))
    arr = [[i, min(X.count(i), Y.count(i))] for i in x if i in y]        
    if len(arr) == 1 and arr[0][0] == '0':
        return '0'
    for i, j in sorted(arr, reverse=True):
        answer += i * j
    return answer if answer != '' else '-1'
