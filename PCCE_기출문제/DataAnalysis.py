def solution(data, ext, val_ext, sort_by):
    arr = {"code":0, "date":1, "maximum":2, "remain":3}
    answer = []
    for i in range(len(data)):
        if data[i][arr[ext]] < val_ext:
            answer.append(data[i])
    answer.sort(key = lambda x : x[arr[sort_by]])
    return answer
