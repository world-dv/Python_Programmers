def solution(s):
    answer = True
    arr = []
    for i in s:
        if i == '(':
            arr.append(i)
        else:
            if '(' not in arr:
                return False
            else:
                arr.pop()
    return answer if len(arr) == 0 else False
