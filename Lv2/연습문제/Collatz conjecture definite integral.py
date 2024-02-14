def solution(k, ranges):        
    arr = goOne(k)
    cal = calculate(arr)
    answer = calRange(len(arr) - 1, cal, ranges)
    return answer

def goOne(k):
    arr = []
    arr.append(k)
    while True:
        if k == 1:
            break
        elif k % 2 == 0:
            k //= 2
        else:
            k = k * 3 + 1
        arr.append(k)
    return arr
            
def calculate(arr):
    cal = []
    #각 구간 1 마다 정적분 값 계산
    #작은수 + (큰 수 - 작은 수) / 2
    for i in range(1, len(arr)):
        cal.append(min(arr[i-1], arr[i]) + abs(arr[i-1] - arr[i]) / 2)
    return cal
    
def calRange(n, cal, ranges):
    answer = []
    for a, b in ranges:
        if b <= 0:
            b = n + b
        if a > b:
            answer.append(-1)
            continue
        total = 0
        for i in cal[a:b]:
            total += i
        answer.append(total)
    return answer
