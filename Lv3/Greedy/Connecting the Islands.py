def solution(n, costs):
    answer = 0
    
    costs = sorted(costs, key = lambda x : x[2])
    parent = [i for i in range(n)]
    rank = [0] * n
    
    for i, edge in enumerate(costs):
        x = find(parent, edge[0])
        y = find(parent, edge[1])
        
        if x != y:
            answer += edge[2]
            union(parent, rank, x, y)
            
    return answer

def find(parent, x):
    if parent[x] == x:
        return x
    
    return find(parent, parent[x])

def union(parent, rank, x, y):
    
    xroot = find(parent, x)
    yroot = find(parent, y)
    
    if rank[xroot] < rank[yroot]:
        parent[xroot] = yroot
    elif rank[xroot] > rank[yroot]:
        parent[yroot] = xroot
    else:
        parent[yroot] = xroot
        rank[xroot] += 1
    
