def solution(n, m):
    answer = []
    a = max(n, m)
    b = min(n, m)
    c = findNumber(a, b)
    answer.append(c)
    answer.append(a * b // c) #최소 공배수 = a * b / 최대공약수
    
    return answer

def findNumber(a, b): #최대 공약수
    for i in range(b, 0, -1):
        if a % i == 0 and b % i == 0:
            return i
