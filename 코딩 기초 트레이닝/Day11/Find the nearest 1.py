def solution(arr, idx):
    answer = arr[idx : ] if len(arr) > idx else -1    
    return answer.index(1) + idx if 1 in answer else -1
