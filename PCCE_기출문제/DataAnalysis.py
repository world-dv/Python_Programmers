def solution(data, ext, val_ext, sort_by):
    arr = {"code":0, "date":1, "maximum":2, "remain":3}
    answer = [[i for i in data[j]] for j in range(len(data)) if data[j][arr[ext]] < val_ext]
    answer.sort(key = lambda x : x[arr[sort_by]])
    return answer
