def solution(n):
    answer = calculate(n)
    return answer

def calculate(x):
    arr = ['4', '1', '2']
    n = ''    
    while x > 0:
        if x == 3:
            n += '4'
            break
        n += arr[x % 3]
        x = x // 3 if x % 3 != 0 else x // 3 - 1
    
    return n[::-1]
    
