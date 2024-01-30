def solution(n, k):
    answer = 0
    a = ''
    while n > 0:
        a += str(n % k)
        n //= k
    a = a[::-1].replace('0', ' ').split(' ')
    
    for i in a:
        if i != '' and prim(int(i)):
            answer += 1
    
    return answer

def prim(x):
    if x < 2:
        return False
    for i in range(2, int(x **(1/2)) + 1):
        if x % i == 0:
            return False
    return True
