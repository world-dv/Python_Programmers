from collections import deque
def solution(maps):
    
    answer = bfs(maps, 'S', 'L')
    answer2 = bfs(maps, 'L', 'E')
    return answer + answer2 if answer != -1 and answer2 != -1 else -1

def bfs(maps, start, target):
    visited = [[0 for _ in range(len(maps[0]))] for _ in range(len(maps))]
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    
    start_p = []
    for i, j in enumerate(maps):
        if start in j:
            start_p = [i, j.index(start), 0]
    
    q = deque()
    q.append(start_p)
    
    while q:
        start_x, start_y, cost = q.popleft()
        
        if maps[start_x][start_y] == target:
            return cost
        for i, j in zip(dx, dy):
            nx, ny = start_x + i, start_y + j
            
            if 0 <= nx < len(maps) and 0 <= ny < len(maps[0]):
                if maps[nx][ny] != 'X' and not visited[nx][ny]:
                    q.append([nx, ny, cost + 1])
                    visited[nx][ny] = 1
    return -1
