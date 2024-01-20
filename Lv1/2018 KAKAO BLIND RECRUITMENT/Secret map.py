def solution(n, arr1, arr2):
    answer = []
    
    for i, j in zip(arr1, arr2):
        a = ord(chr(i))
        b = ord(chr(j))
        c = format(a | b, 'b').replace('0', ' ').replace('1', '#')
        if len(c) < n:
            c = ' ' * (n - len(c)) + c
        answer.append(c)
    
    return answer
