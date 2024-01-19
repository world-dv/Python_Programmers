def solution(s):
    answer = []
    arr = []
    a = []
    n = ''
    for i in s:
        if i.isdecimal():
            n += i
        elif i == ',':
            if n != '':
                a.append(n)
            n = ''
        elif i == '}':
            if n != '':
                a.append(n)
                arr.append(a)
            n = ''
            a = []
    arr.sort(key = len)
    
    for i in arr:
        for j in i:
            if int(j) not in answer:
                answer.append(int(j))
    
    return answer
