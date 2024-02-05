def solution(data, col, row_begin, row_end):
    answer = 0
    
    data = sorted(data, key = lambda x : (x[col-1], -x[0]))
    
    for i in range(row_begin-1, row_end):
        a = 0
        for j in data[i]:
            a += j % (i+1)
        answer = answer ^ a
    
    return answer
