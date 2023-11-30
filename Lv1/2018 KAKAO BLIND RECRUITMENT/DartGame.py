import re
def solution(dartResult):
    arr = []
    dart = re.split('([S|D|T|*|#])', dartResult)
    dic = { 'S' : 1, 'D' : 2, 'T' : 3 }
    for i in dart:
        if i == '':
            continue
        elif i.isdigit():
            arr.append(int(i))
        elif i == '*':
            arr[-1] = arr[-1] * 2
            if arr[0] != arr[-1]:
                arr[-2] = arr[-2] * 2
        elif i == '#':
            arr[-1] = arr[-1] * (-1)
        else:
            arr[-1] = arr[-1] ** dic[i]
    answer = sum(arr)
    return answer
