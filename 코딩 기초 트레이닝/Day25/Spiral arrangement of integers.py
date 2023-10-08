def solution(n):
    answer = [[0 for i in range(n)] for j in range(n)]
    a = 1
    r_b = 0
    e_r_b = n - 1
    c_b = 0
    e_c_b = n - 1
    while a <= n * n :
        #왼->오
        for j in range(c_b, e_c_b + 1):
            if answer[r_b][j] == 0:
                answer[r_b][j] = a
                a += 1
        r_b += 1
        #위->아래
        for j in range(r_b, e_r_b + 1):
            if answer[j][e_c_b] == 0:
                answer[j][e_c_b] = a
                a += 1
        e_c_b -= 1
        #오->왼    
        for j in range(e_c_b, c_b -1, -1):
            if answer[e_r_b][j] == 0:
                answer[e_r_b][j] = a
                a += 1
        e_r_b -= 1
        #아래->위
        for j in range(e_r_b, r_b-1, -1):
            if answer[j][c_b] == 0:
                answer[j][c_b] = a
                a += 1
        c_b += 1
    return answer
