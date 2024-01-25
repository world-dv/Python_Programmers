def solution(word):
    global arr
    answer = 0
    arr = []
    dfs(word[0], 0)
    a = {'A' : 1, 'E' : 782, 'I' : 1563, 'O': 2344, 'U' : 3125}
    answer += arr.index(word) + a[word[0]]
    return answer

def dfs(word, count):
    global answer
    
    if word not in arr:
        arr.append(word)
    count += 1
    if count >= 5:
        word = ''
        return 
    
    for i in 'AEIOU':
        dfs(word+i, count)
