def solution(myString, pat):
    pat = ''.join(['A' if i == 'B' else 'B' for i in pat])
    answer = int(pat in myString)
    return answer
