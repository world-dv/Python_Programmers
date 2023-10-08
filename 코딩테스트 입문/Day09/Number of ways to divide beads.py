def solution(balls, share):
    answer = 1 
    for i, j in zip(range(share+1, balls + 1), range(1, balls - share + 1)) :
        answer = answer * i // j
    return answer
