from functools import cmp_to_key
def solution(numbers):
    numbers = list(map(str, numbers))
    numbers = sorted(numbers, key = cmp_to_key(lambda a, b : compare(a, b)))
    answer = ''.join(numbers)
    return answer if int(answer) != 0 else '0'

def compare(x, y):
    a = int(x + y) #ex) '1' + '2' = '12'
    b = int(y + x) #ex) '2' + '1' = '21'
    return (b > a) - (b < a) #'21' > '12'이므로 '21' - '12' - ... 
