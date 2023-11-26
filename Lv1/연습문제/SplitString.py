def solution(s):
    answer = 0
    arr = []
    for i in range(len(s)):
        arr.append(s[i])
        l = arr.count(arr[0])
        if l == len(arr) - l:
            answer += 1
            arr = []
    return answer + (1 if arr else 0)
