def solution(ingredient):
    answer = 0
    arr = []
    for i in ingredient:
        arr.append(i)
        if arr[-4:] == [1, 2, 3, 1]:
            answer += 1
            arr.pop(-4)
            arr.pop(-3)
            arr.pop(-2)
            arr.pop(-1)
    return answer
