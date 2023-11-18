def solution(arr):
    answer = arr[0]

    for i in range(1, len(arr)):
        l = gcd(answer, arr[i])
        answer = answer * arr[i]
        if (l > 0):
            answer //= l
    return answer

def gcd(a, b):
    for i in range(max(a, b), 1, -1):
        if a % i == 0 and b % i == 0:
            return i
    return 0
