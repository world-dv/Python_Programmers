from collections import deque
def solution(rectangle, characterX, characterY, itemX, itemY):
    answer = 0
    
    graph = [[-1 for _ in range(102)] for _ in range(102)]
    
    for rect in rectangle:
        x1, y1, x2, y2 = map(lambda x : x * 2, rect)
        for x in range(x1, x2+1):
            for y in range(y1, y2+1):
                if x1 < x < x2 and y1 < y < y2:
                    graph[x][y] = 0
                elif graph[x][y] != 0:
                    graph[x][y] = 1
    
    answer = bfs(graph, characterX * 2, characterY * 2, itemX * 2, itemY * 2)
    
    return answer

def bfs(graph, x, y, ix, iy):
    answer = 0
    dist = [[1 for _ in range(102)] for _ in range(102)]
    
    q = deque()
    q.append([x, y])
    
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    
    while q:
        x, y = q.popleft()
    
        if x == ix and y == iy:
            answer = dist[x][y] // 2
            break
    
        for i, j in zip(dx, dy):
            nx = x + i
            ny = y + j
            
            if graph[nx][ny] == 1 and dist[nx][ny] == 1:
                dist[nx][ny] += dist[x][y]
                q.append([nx, ny])
    return answer
    
