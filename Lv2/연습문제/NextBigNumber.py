def solution(n):
    answer = n + 1
    count = str(bin(n)).count('1')
    while True:
        if bin(answer).count('1') == count:
            break
        answer += 1
    return answer
