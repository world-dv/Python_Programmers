def solution(arr):
    arr.remove(min(arr))
    answer = arr
    return answer or [-1]
