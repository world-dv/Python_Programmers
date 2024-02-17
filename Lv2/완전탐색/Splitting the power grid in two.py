def solution(n, wires):
    answer = n
    
    graph = [[] for _ in range(n+1)]
    for a, b in wires:
        graph[a].append(b)
        graph[b].append(a)
    
    def dfs(node, parent):
        cnt = 1
        for n in graph[node]:
            if n != parent:
                cnt += dfs(n, node)
        return cnt
    
    for a, b in wires:
        graph[a].remove(b)
        graph[b].remove(a)
        
        node_a = dfs(a, b)
        node_b = n - node_a
        
        answer = min(answer, abs(node_a - node_b))
        
        graph[a].append(b)
        graph[b].append(a)
    
    return answer
