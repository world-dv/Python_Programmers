from collections import deque

def solution(maps):
    answer = []

    graph = [[int(i) if i != 'X' else 0 for i in m] for m in maps]
    
    def bfs(x, y):
        q = deque()
        q.append([x,y])
        
        dx = [0, 1, 0, -1]
        dy = [1, 0, -1, 0]
        
        total = 0
        
        while q:
            x, y = q.popleft()
            
            for i, j in zip(dx, dy):
                nx, ny = x + i, y + j
                if 0 <= nx < len(graph) and 0 <= ny < len(graph[0]):
                    if graph[nx][ny]:
                        total += graph[nx][ny]
                        q.append([nx, ny])
                        graph[nx][ny] = 0
        if total == 0:
            total += graph[x][y]
            graph[x][y] = 0
        return total
    
    for i in range(len(graph)):
        for j in range(len(graph[i])):
            if graph[i][j]:
                answer.append(bfs(i, j))
    return sorted(answer) or [-1]
