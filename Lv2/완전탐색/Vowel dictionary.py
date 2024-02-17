def solution(word):
    global answer, count
    answer = 0
    count = 0
    
    def dfs(start, n, target):
        global answer, count
        count += 1
        if target == start:
            answer = count
        if len(start) == n:
            return
        for i in 'AEIOU':
            dfs(start+i, n, target)
            
    dfs(word[0], 5, word)
    
    for i in 'AEIOU':
        if i == word[0]:
            break
        answer += 781
    
    return answer
