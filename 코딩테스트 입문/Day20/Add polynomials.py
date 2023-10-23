def solution(polynomial):
    polynomial = polynomial.split(' ')
    answer = ''
    a, b = 0, 0
    for i in polynomial:
        if 'x' in i:
            a += int(i[:i.index('x')]) if i[:i.index('x')] != '' else 1
        if 'x' not in i and i != '+' :
            b += int(i) if i != '' else 0
    
    a = a if a != 1 else ''
    if a == 0:
        answer = str(b) if b != '' else '0'
    elif b == 0:
        answer = str(a) + 'x'
    else:
        answer = str(a) + 'x + ' + str(b)
    return answer
