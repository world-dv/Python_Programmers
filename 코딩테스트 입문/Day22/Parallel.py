def solution(dots):
    answer = 0
    arr = []
    for i in range(len(dots) - 1):
        visited = [0, 0, 0, 0]
        visited[0] = 1
        visited[i+1] = 1
        
        ax = dots[0][0] #x1
        ay = dots[0][1]
        
        bx = dots[i+1][0] #x2
        by = dots[i+1][1]
        
        c = visited.index(0)
        cx = dots[c][0] #x3
        cy = dots[c][1]
        
        d = visited.index(0, visited.index(0)+1)
        dx = dots[d][0] #x4
        dy = dots[d][1]
        
        if ((by-ay)/(bx-ax) == (dy-cy)/(dx-cx)):
            return 1
    
    return answer
