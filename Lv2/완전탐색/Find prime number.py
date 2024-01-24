def solution(numbers):
    global arr
    arr = []
    answer = 0
    
    for idx, i in enumerate(numbers):
        visited = [0 for i in range(len(numbers))]
        dfs(numbers, visited, i, idx)
    answer = len(arr)
    return answer

def dfs(numbers, visited, i, idx):
    visited[idx] = 1
    if findPrm(int(i)) and str(int(i)) == i and i not in arr:
        arr.append(i)
    for idx2, a in enumerate(numbers):
        if not visited[idx2]:
            dfs(numbers, visited, i + a, idx2)
            visited[idx2] = 0

def findPrm(x):
    if x == 0 or x == 1:
        return False
    for i in range(2, x):
        if x % i == 0:
            return False
    return True
