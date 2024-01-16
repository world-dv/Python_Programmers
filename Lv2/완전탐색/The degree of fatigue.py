def solution(k, dungeons):
    global answer
    answer = []
    for i in range(len(dungeons)):
        visited = [0] * len(dungeons)
        dfs(k, i, visited, dungeons)
    return max(answer)

def dfs(k, i, visited, dungeons):
    visited[i] = 1
    k = k - dungeons[i][1]
    answer.append(sum(visited))
    for a in range(len(dungeons)):
        if not visited[a] and dungeons[a][0] <= k:
            dfs(k, a, visited, dungeons)
            visited[a] = 0
