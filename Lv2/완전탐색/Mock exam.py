def solution(answers):
    arr = [0] * 3
    answer = []
    s1 = [1,2,3,4,5] * calLen(len(answers), 5)
    s2 = [2,1,2,3,2,4,2,5] * calLen(len(answers), 8)
    s3 = [3,3,1,1,2,2,4,4,5,5] * calLen(len(answers), 10)
    
    for i in range(len(answers)):
        if answers[i] == s1[i]:
            arr[0] += 1
        if answers[i] == s2[i]:
            arr[1] += 1
        if answers[i] == s3[i]:
            arr[2] += 1
            
    m = max(arr)
    for i, j in enumerate(arr):
        if j == m:
            answer.append(i+1)
    return answer

def calLen(x, s):
    if x % s == 0:
        return x // s
    return x // s + 1
