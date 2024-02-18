def solution(number, k):
    answer = ''
    n = k
    arr = []
    for i in number:
        while arr and n > 0 and arr[-1] < i:
            arr.pop()
            n -= 1
        arr.append(i)
    answer = ''.join(arr[:len(number) - k])
    return answer
