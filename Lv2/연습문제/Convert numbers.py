from collections import deque
def solution(x, y, n):
    answer = bfs(x, y, n)
    return answer

def bfs(x, y, n):
    q = deque([x])
    visited = [0] * (y + 1)
    visited[x] = 1
    while q:
        a = q.popleft()
        
        if 0 <= a + n <= y and visited[a + n] == 0:
            visited[a + n] = visited[a] + 1
            q.append(a + n)
        if 0 <= a * 2 <= y and visited[a * 2] == 0:
            visited[a * 2] = visited[a] + 1
            q.append(a * 2)
        if 0 <= a * 3 <= y and visited[a * 3] == 0:
            visited[a * 3] = visited[a] + 1
            q.append(a * 3)
    return visited[y] - 1
