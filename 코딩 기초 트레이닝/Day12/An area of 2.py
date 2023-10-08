def solution(arr):
    if 2 not in arr :
        return [-1]
    answer = arr[arr.index(2):len(arr) - arr[::-1].index(2)]
    return answer
