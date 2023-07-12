def solution(n, computers):
    answer = 0
    visited = [False for i in range(n)]
    def dfs(computers, v):
        visited[v] = True
        for i in range(n):
            if not visited[i] and computers[v][i]:
                dfs(computers, i)

    for i in range(n):
        if not visited[i]:
            dfs(computers, i)
            answer += 1
            
    return answer
