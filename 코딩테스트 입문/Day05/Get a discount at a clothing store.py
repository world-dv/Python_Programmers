def solution(price):
    answer = 1
    if price >= 500000:
        answer = 0.8
    elif price >= 300000:
        answer = 0.9
    elif price >= 100000:
        answer = 0.95
    answer = int(answer * price)
    return answer
