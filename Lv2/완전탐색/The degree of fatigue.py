def solution(k, dungeons):
    answer = []
    visited = [0 for _ in range(len(dungeons))]
    
    def dfs(hp, visited):
        if sum(visited) not in answer:
            answer.append(sum(visited))
        if hp <= 0:
            return
        for i, j in enumerate(dungeons):
            if not visited[i] and hp >= j[0]:
                visited[i] = 1
                dfs(hp - j[1], visited)
                visited[i] = 0
        
    dfs(k, visited)
    return max(answer)
