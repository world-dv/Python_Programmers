from collections import defaultdict, deque 
def solution(n, edge):
    answer = bfs(n, edge)
    return answer

def bfs(n, edge):
    edge_list = defaultdict(list)
    for i, j in edge:
        edge_list[i].append(j)
        edge_list[j].append(i)
    
    visited = [0] * (n+1)
    weight = [0] * (n+1)
    
    q = deque()
    q.append(1)
    
    while q:
        start = q.popleft()
        visited[start] = 1
        for i in edge_list[start]:
            if not visited[i]:
                q.append(i)
                visited[i] = 1
                weight[i] = weight[start] + 1
    return weight.count(max(weight))
