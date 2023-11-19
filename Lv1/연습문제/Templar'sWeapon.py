def solution(number, limit, power):
    answer = 0
    for i in range(1, number+1):
        a = countFactor(i)
        answer += power if a > limit else a
    return answer

def countFactor(x):
    arr = []
    for i in range(1, int((x + 1) ** (1/2)) + 1):
        if x % i == 0:
            arr.append(i)
            arr.append(x // i)
    return len(set(arr))
