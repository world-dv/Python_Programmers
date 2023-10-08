def solution(absolutes, signs):
    answer = sum([i if j else i * -1 for i,j in zip(absolutes, signs)])
    return answer
