def solution(want, number, discount):
    answer = 0
    for i, j in enumerate(discount):
        arr = [discount[i:i+10].count(z) for z in want]
        compare_arr = [a <= b for a, b in zip(number, arr)]
        if compare_arr.count(True) == len(want):
            answer += 1
    return answer
