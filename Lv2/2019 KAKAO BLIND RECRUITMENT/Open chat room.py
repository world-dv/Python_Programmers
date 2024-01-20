def solution(record):
    answer = []
    dic = dict()
    i = 0
    for i in record:
        a = i.split(' ')
        if a[0] == 'Enter':
            dic[a[1]] = a[2]
        if a[0] == 'Leave':
            continue
        if a[0] == 'Change':
            dic[a[1]] = a[2]
        
    for i in record:
        a = i.split(' ')
        b = ''
        if a[0] == 'Enter':
            b = dic[a[1]] + '님이 들어왔습니다.'
        if a[0] == 'Leave':
            b = dic[a[1]] + '님이 나갔습니다.'
        if a[0] == 'Change':
            continue
        answer.append(b)
    return answer
