def solution(myString, pat):
    answer = 0
    for i, j in enumerate(myString):
        if pat in myString[i:i+len(pat)]:
            answer += 1
    return answer
