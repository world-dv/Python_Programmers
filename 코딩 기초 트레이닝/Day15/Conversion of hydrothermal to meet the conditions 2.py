import copy
def solution(arr):
    answer = 0
    arr2 = []
    while(arr2 != arr):
        arr2 = copy.deepcopy(arr)
        for j, i in enumerate(arr):
            if i % 2 == 0 and i >= 50:
                arr[j] = i // 2
            elif i % 2 != 0 and i < 50:
                arr[j] = i * 2 + 1
        answer += 1
    return answer - 1
